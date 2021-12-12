from requests_html import HTMLSession
import wget
import time
from tqdm import tqdm


s = HTMLSession()

headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'}

print('WRITING GOOGLE PATENTs...')

file = open('Input.txt', 'r')
patents = file.readlines()
out = 'Downloaded patents'
for patent in tqdm(patents):
    try:
        r = s.get(patent.strip(), headers=headers)
        r.html.render(sleep=5, timeout=50)
        pdf_url = r.html.find('div.knowledge-card-action-bar.style-scope.patent-result')
        for url in pdf_url:
            link = url.find('a.style-scope.patent-result', first=True).attrs['href']
            wget.download(link, out=out)
            
    except:
        pass

    time.sleep(2)    
    

input()
