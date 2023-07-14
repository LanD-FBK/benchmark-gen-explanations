from bs4 import BeautifulSoup
import requests
from multiprocessing import Pool
import tqdm
import time
import json


def scrape_article(url):
    source = requests.get(url)
    soup = BeautifulSoup(source.text, features="lxml")
    try:
        article_container = soup.find('article', class_='m-textblock')
        par = article_container.find_all('p')
        par = [el.get_text().strip() for el in par]
        if len(par) == 0 or (len(par) == 1 and par[0] == ""): 
            par = [article_container.get_text()]
        return {"ID" : url.split('/')[-1], "ARTICLE" : par}
    except:
        return {"ID" : url.split('/')[-1], "ARTICLE" : ["ERROR"]}


print('Getting URLs...')
base_url = 'http://www.politifact.com/factchecks/'
with open('../data/ids/ids.txt', 'r', encoding='utf-8') as file:
    ids = file.read().split('\n')
    file.close()
urls = [base_url + ID for ID in ids]

print('Scraping the articles...')
start = time.time()
p = Pool(11)
# results = p.map(scrape_article, urls)
results = list(tqdm.tqdm(p.imap(scrape_article, urls), total=len(urls)))
p.terminate()
p.join()
end = time.time()
print(f'Scraping runtime is {end - start}')

print('Saving results...')
with open('articles.json', "w", encoding='utf-8') as out:
    json.dump(results, out, indent=4)
    out.close()

print('END')