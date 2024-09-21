import requests
from bs4 import BeautifulSoup

def scrape_bbc_news():
    """
    Scrapes the BBC News website for article titles and their corresponding links.
    """
    url = "https://www.bbc.com/news"  
    response = requests.get(url)
    bbc_web_page = response.text

    soup = BeautifulSoup(bbc_web_page, "html.parser")
    articles = soup.find_all("a", {"data-testid": "internal-link"})

    article_texts = []
    article_links = []
    for article in articles:
        title = article.find("h2", {"data-testid": "card-headline"})
        if title:
            article_texts.append(title.get_text())
            article_links.append("https://www.bbc.com" + article.get("href"))

    return article_texts, article_links

if __name__ == "__main__":
    titles, links = scrape_bbc_news()
    for title, link in zip(titles, links):
     print(f"Title: {title}\nURL: {link}\n")