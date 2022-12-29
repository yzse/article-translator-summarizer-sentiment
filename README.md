# News Article Translator, Summarizer, & Sentiment Analyzer
Scrapes, translates, summarizes, and analyzes sentiment from El País, one of the most circulated newspapers in Spain.

**Contents**
- [Content](#content)
- [Usage](#usage)
- [Sample Output](#sample-output)

## Content
This project summarises Spanish news in English using an end-to-end pipeline:  runs a web scraper, translates from Spanish to English using `Helsinki-NLP`, summarizes using Google's `Pegasus-xsum`, and analyzes sentiment using `BERT`.

## Usage
Install the latest version for a stable release.

```bash
python scraper.py # scrape primary data
python summarizer.py # runs summarizing pipeline
```

## Sample Output
The script outputs a .CSV file, along with the article's translation, summary, and sentiment analysis.  By default, the script analyses the top 5 headlines of the day.  See below for a sample format, the translated text has been truncated for this markdown.


  |date      | title_es        | translation        | summary        | sentiment label      | sentiment score      |
  |----------|-----------------|--------------------|----------------|----------------------|----------------------|
  |12-29-2022|Guerra entre Ucrania y Rusia: Últimas noticias en directo: Ucrania asegura haber derribado 54 de los 69 misiles del ataque ruso contra infraestructuras energéticas|Kiev, Járkov, Odessa and Yitomir record explosions causing at least three injuries in the capital  Belarus summons the Ukrainian ambassador and demands “exhaustive investigation” by the fall of a missile on its territory...|The BBC's Russia correspondent assesses the latest developments in the Ukraine-Belarus conflict.|NEU|0.9750946760177610|
  |12-29-2022|Rusia lanza uno de los mayores ataques de la guerra contra las infraestructuras energéticas de Ucrania|On the eve of the celebrations to receive the new year, Russia has launched a missile rain on Ukraine this Thursday. The sound of the explosions has resounded since shortly after dawn in towns and cities throughout the country. The attack, with 69 cruise missiles and drone bombs...|A missile rain on New Year's Eve leaves 90 percent of the homes in the city of Lviv and 40 percent of the homes in Kiev out of light.|NEU|0.626018404960632|
  |12-29-2022|Alarma en Interior tras el asesinato de tres mujeres en menos de 24 horas|In more than half of the 11 deaths recorded in December, there were previous reports of a macho murder every 20 hours, six murders in five days, three in the last 24 hours. That's the count since last Saturday. The most recent ones, in Castilla-La Mancha, Madrid and Benidorm. On the afternoon of last Wednesday, in Escalona (Toledo), a 52-year-old man murdered his 32-year-old wife, pregnant with another partner and a week after giving birth. She shared with him who was her alleged murderer a daughter of 14 and a son of 13 who stood before her when she killed her; it was the youngest who called 112...|The last week in Spain has seen a dramatic rise in the number of macho murders: 11 in 28 days, six of them well-introduced by the victims against whom their murderers have now been, or by the victims against previous couples.|NEG|0.8540323376655580|
  |12-29-2022|La UE permanece vigilante mientras Italia reclama ya un mecanismo común para controlar a los pasajeros desde China|Washington, Rome and Tokyo impose restrictions on airports. The WHO Director for Europe underlines the importance of countries sharing information about the virus The tsunami of covid infections that China is experiencing has raised the alarm in the rest of the world. Several countries, including the United States, have decided to impose restrictions on travellers from China, after Beijing announced the end of quarantines for international travellers. The Health Safety Committee of the European Commission met this Thursday to “coordinate” the response of the 27 to the situation, although no concrete decisions have emerged from the quote...|The World Health Organization (WHO) has called for “coordination of national responses to cross-border health threats” in the wake of the outbreak of the coronavirus in China.|NEU|0.9654762744903560|
  |12-29-2022|El virólogo Luis Enjuanes: “La situación en China es preocupante y tendrá efecto cascada en el resto del mundo”|The researcher considers it a mistake that the country has suddenly passed and with low vaccination coverage from one policy to another almost unfettered Three years after the start of the coronavirus pandemic, the world looks again at China in fear. The explosion of cases in the Asian giant after the abrupt end of the zero-covid policy, which has been in effect since 2020, has sparked concern in many governments. The question is how an uncontrolled increase in contagion can affect the globe in a country with more than 1.4 billion inhabitants. Luis Enjuanes (Valencia, 77), director of the coronavirus laboratory...|Luis Enjuanes, director of the coronavirus laboratory at Spain's National Center for Biotechnology (CNB-CSIC), explains why the world is worried about China.|NEU|0.9480028748512270|

