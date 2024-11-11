import requests
from bs4 import BeautifulSoup

def scrape_site(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        headlines = [h.get_text() for h in soup.find_all("h1")]
        paragraphs = [p.get_text() for p in soup.find_all("p")]
        return {"headlines": headlines, "paragraphs": paragraphs}
    except Exception as e:
        return {"error": str(e)}
