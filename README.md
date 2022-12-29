# news-translator-summarizer-sentiment
Scrapes, translates, summarizes, and analyzes sentiment from El País (Spain) using a Hugging Face translator, Google Pegasus, and BERT.

**Contents**
- [Content](#content)
- [Installation](#installation)

## What is `lumpia`?
This project summarises Spanish news in English using an end-to-end pipelines:  run a scraper, translates from Spanish to English using `Helsinki-NLP`, summarizes using Google's `Pegasus-xsum`, and analyzes sentiment using `BERT`.

## Run
Install the latest version for a stable release.

```bash
pip install -U git+https://github.com/yzse/es-news-translator-summarizer-sentiment
python scraper.py # scrape primary data
python summarizer.py # runs summarizing pipeline
```
