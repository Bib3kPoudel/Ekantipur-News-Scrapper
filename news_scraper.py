import requests
from bs4 import BeautifulSoup




def ekantipur_news():
    html_text = requests.get('https://ekantipur.com/').text
    soup = BeautifulSoup(html_text,'lxml')


    #major headlines section
    news_card = soup.find_all('h1')
    print('Major Headlines:')
    for headlines in news_card:
        major_headlines = headlines.find_all('a')
        
        for headline in major_headlines:
            link = headline['href']
            print(f'{headline.text.strip()}')
            print(f'More: {link}')


    #banner section
    print("\n--------------------------------------------------------------\n")
    news = soup.find_all('div', class_="more-main-news")
    for div in news:
        articles =div.find_all('article',class_="normal ui-draggable ui-draggable-handle ui-droppable")
        for article in articles:
            link = article.h2.a['href']
            print(f"{article.h2.text.strip()}:\n{article.p.text.strip()}\nMore: {link}\n")
            
            
    #samachar section
    news2 = soup.find_all('div', class_="col-xs-10 col-sm-10 col-md-10")
    for article in news2:
        articles = article.find_all('article', class_="normal")
        for samachar in articles:
            link= samachar.h2.a['href']
            print(f"{samachar.h2.text.strip()}:\n{samachar.p.text.strip()}\nMore: {link}\n")
        
if __name__=="__main__":    
    ekantipur_news()

