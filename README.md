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
The script outputs a `csv` file, along with the article's translation, summary, and sentiment analysis.  See below for a sample format:


  | title_es        | translation        | summary        | sentiment label      | sentiment score      |
  |-----------------|--------------------|----------------|----------------------|----------------------|

