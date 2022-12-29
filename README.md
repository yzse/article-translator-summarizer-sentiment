# news-translator-summarizer-sentiment
Scrapes, translates, summarizes, and analyzes sentiment from El País, one of the most circulated newspapers in Spain.

**Contents**
- [Content](#content)
- [Usage](#usage)
- [Sample Output](#sample-output)

## Content
This project summarises Spanish news in English using an end-to-end pipelines:  run a scraper, translates from Spanish to English using `Helsinki-NLP`, summarizes using Google's `Pegasus-xsum`, and analyzes sentiment using `BERT`.

## Usage
Install the latest version for a stable release.

```bash
pip install -U git+https://github.com/yzse/es-news-translator-summarizer-sentiment
python scraper.py # scrape primary data
python summarizer.py # runs summarizing pipeline
```

## Sample Output
The script outputs a `csv` file, along with the article's translation, summary, and sentiment analysis.  By default, the script analyses the top 5 headlines of the day.  See below for a sample format:


  | title_es        | translation        | summary        | sentiment label      | sentiment score      |
  |-----------------|--------------------|----------------|----------------------|----------------------|
  |Guerra entre Ucrania y Rusia: Últimas noticias en directo: Ucrania asegura haber derribado 54 de los 69 misiles del ataque ruso contra infraestructuras energéticas|Kiev, Járkov, Odessa and Yitomir record explosions causing at least three injuries in the capital  Belarus summons the Ukrainian ambassador and demands “exhaustive investigation” by the fall of a missile on its territory|The BBC's Russia correspondent assesses the latest developments in the Ukraine-Belarus conflict.|NEU|0.9750946760177610|
