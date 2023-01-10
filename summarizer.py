from transformers import pipeline
from datetime import date, datetime
import nltk, glob, os, csv

nltk.download("punkt") 
today = date.today().strftime('%m-%d-%Y')

# 0. Helper function
def split(text: str): # split article into sentences for handling long articles
    sentences = nltk.tokenize.sent_tokenize(text, "english")
    return sentences

# 1. Read articles
def get_articles(input_file):
    ret = ''
    with open(input_file, 'r') as file:
        title = file.readline()
        ret = file.read().strip('\n')
    return title, ret

# 2. Translate articles
def translate(split_list: list): 
    trans_results = []
    for sentence in split_list:
        trans = []
        translator = pipeline("translation", model="Helsinki-NLP/opus-mt-es-en") 
        for i in translator(sentence):
            trans.append(i['translation_text'])
        trans_results.append(trans)
    res = sum(trans_results, [])
    res = ' '.join(str(s) for s in res)
    return res 

# 3. Summarize all translated articles using Google Pegasus
def summarize(input_text):
    summ_results = []
    summarizer = pipeline("summarization", model="google/pegasus-xsum")
    for i in summarizer(input_text, min_length=20, max_length=80, truncation=True):
        summ_results.append(i['summary_text'])
    return summ_results 

# 4. Adding sentiment analysis using Bert
def get_sentiment(input_text): 
    sentiment = pipeline("sentiment-analysis", model="finiteautomata/bertweet-base-sentiment-analysis")
    score = sentiment(input_text)
    return score

# 5.0 Helper function for export
def run_pipeline(latest_files, numArticles):

    res_list = []
    count = 1

    for file in latest_files:
        print('{:%H:%M} working on {}/{} articles...'.format(datetime.now(), count, numArticles))
        title_es, article = get_articles(file)
        splitted = split(article)

        print('{:%H:%M} translating...'.format(datetime.now()))
        translated = translate(splitted)

        print('{:%H:%M} summarizing...'.format(datetime.now()))
        summarized = summarize(translated)[0]
        if len(summarized) > 80:
            summarized = summarize(summarized)[0]

        print('{:%H:%M} scoring...'.format(datetime.now()))
        score = get_sentiment(summarized)

        count += 1 
        res = {
            'date': today,
            'title_es': title_es,
            'translation': translated,
            'summary': summarized,
            'sentiment label': score[0]['label'],
            'sentiment score': score[0]['score']
        }
        res_list.append(res)

    # output to csv
    keys = res_list[0].keys()
    with open('outputs/elpais_summary_{}.csv'.format(today), mode='w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(res_list)
    
    return res_list

# 5.1 Export Results
def create_output_array(numArticles: int):    
    search_dir = 'news-articles/' + today + '/'
    
    # remove videos and podcasts
    to_remove = ['Vídeo', 'Podcast']
    for file in glob.glob(search_dir):
        if any(x in file for x in to_remove):
            os.remove(file)
    
    # pull top 10 headlines of the day
    files = list(filter(os.path.isfile, glob.glob(search_dir + '*')))
    files.sort(key=lambda x: os.path.getmtime(x))
    latest_files = files[:numArticles]
    output_csv = run_pipeline(latest_files, numArticles)

    return output_csv

def run():
    create_output_array(10)

if __name__ == '__main__':
    run()
