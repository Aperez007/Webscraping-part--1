from bs4 import BeautifulSoup
import requests
    
with open('sample.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# print(soup.prettify()) #lines up code in terminal

# match = soup.title.text
# print(match)

for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print()