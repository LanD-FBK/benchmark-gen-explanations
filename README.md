# Benchmarking the Generation of Fact Checking Explanations

This repository contains the code necessary to recreate the datasets employed in **Benchmarking the Generation of Fact Checking Explanations**, namely **LIAR++** and **FullFact** datasets. If you use these datasets or any partial sections of them in your work, we kindly request that you cite our original paper.

- [LIAR++](#liar_plus_plus)
- [FullFact](#fullfact)
- [License](#license)
- [References](#references)

---

## LIAR++

We created LIAR++ starting from the LIAR-PLUS dataset [Alhindi et al., EMNLP 2018](https://aclanthology.org/W18-5513). LIAR-PLUS contains some entries in which the verdict was artificially created by extracting the last five sentences from the body of the article (silver data). In all the other cases, verdicts were extracted from a specific section of web pages, usually titled *Our ruling* or *Summing up* (gold data). LIAR-PLUS is publicly available and can be found [here](https://github.com/Tariq60/LIAR-PLUS). This dataset does not contain the articles' text, and POLITIFACT APIs are no longer available. To retrieve this information we leveraged the data IDs and scraped from scratch the articles. In the [data](https://github.com/drusso98/fake_news/tree/main/liar_dataset/data) folder we provide a list of all the LIAR-PLUS IDs as well as the list of the IDs of the gold data employed in our experiments (divided in test, train, and validation set). We also provide the [code](https://github.com/drusso98/fake_news/blob/main/liar_dataset/scraper.py) employed for scraping the articles from [PolitiFact website](https://www.politifact.com).

<img src="liar_dataset/politifact_example.drawio.png" width="70%">

## FullFact
With a similar procedure to that used for LIAR++, we created a new dataset starting from the [FullFact website](https://fullfact.org). This dataset
contains data spanning from 2010 to 2021 and covers several different topics, such as health, economy, crime, law, and education. In FullFact the verdict is always present as a separate element in the web page so there was no need to filter the data. This dataset accounts for 1838 claim-article-verdict triples. Data were obtained by scraping from the website pages the necessary information. In the data folder, we provide the list of the links to the FullFact articles used for building our dataset (divided into test, train, and validation sets). 

<img src="liar_dataset/fullfact_example.drawio.png" width="70%">


## References
- Tariq Alhindi, Savvas Petridis, and Smaranda Muresan. 2018. Where is Your Evidence: Improving Fact-checking by Justification Modeling. In Proceedings of the First Workshop on Fact Extraction and VERification (FEVER), pages 85–90, Brussels, Belgium. Association for Computational Linguistics.

---
For any questions or inquiries, please contact drusso@fbk.eu
