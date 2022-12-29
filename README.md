# news-translator-summarizer-sentiment
Scrapes, translates, summarizes, and analyzes sentiment from El País, one of the most circulated newspapers in Spain.

**Contents**
- [Content](#content)
- [Installation](#installation)

## Content
This project summarises Spanish news in English using an end-to-end pipelines:  run a scraper, translates from Spanish to English using `Helsinki-NLP`, summarizes using Google's `Pegasus-xsum`, and analyzes sentiment using `BERT`.

## Installation
Install the latest version for a stable release.

```bash
pip install -U git+https://github.com/yzse/es-news-translator-summarizer-sentiment
python scraper.py # scrape primary data
python summarizer.py # runs summarizing pipeline
```
