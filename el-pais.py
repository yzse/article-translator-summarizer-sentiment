import requests
import lxml.html as html
import os
import datetime

HOME_URL = 'https://www.elpais.com/'
XPATH_LINK_TO_ARTICLE = '//h2[@class="c_t "]/a/@href'
XPATH_TITLE = '//h1[@class="a_t"]/text()'
XPATH_SUMMARY = '//h2[@class="a_st"]/text()'
XPATH_BODY = '//div[@class="a_c clearfix"]/p//text()'

def parse_notice(link, today):
    try:
        response = requests.get(f'https://elpais.com/{link}')
        if response.status_code == 200:
            notice = response.content.decode('utf-8')
            parsed = html.fromstring(notice)

            try:
                title = parsed.xpath(XPATH_TITLE)[0].replace('\"', '')
                sumary = parsed.xpath(XPATH_SUMMARY)[0]
                body = parsed.xpath(XPATH_BODY)
            except IndexError:
                return

            with open(f'{today}/{title}.txt', 'w', encoding='utf-8') as f:
                f.write(title)
                f.write('\n\n')
                f.write(sumary)
                f.write('\n\n')

                paragraph = ''
                for p in body:
                    paragraph += p
                    if p.endswith('.'):
                        f.write(paragraph)
                        f.write('\n\n')
                        paragraph = ''
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)


def parse_home():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            links_to_notices = parsed.xpath(XPATH_LINK_TO_ARTICLE)
            print(len(links_to_notices))
            today = datetime.date.today().strftime('%m-%d-%Y')
            if not os.path.isdir(today):
                os.mkdir(today)
            for link in links_to_notices:
                parse_notice(link, today)
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)

def run():
    parse_home()

if __name__ == '__main__':
    run()