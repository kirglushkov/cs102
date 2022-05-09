import requests
from bs4 import BeautifulSoup
domain = "https://news.ycombinator.com/"


def extract_news(parser):
    """Extract news from a given web page"""
    body = parser.findAll('table')[2]
    authors = [user.text for user in body.findAll("a", {"class": "hnuser"})]
    links = [link["href"] for link in body.findAll("a", {"class": "titlelink"})]
    urls = []
    for url in links:
        urls.append(domain + url if url[:4] == "item" else url)
    points = [score.text.split()[0] for score in body.findAll("span", {"class": "score"})]
    ids = [post["id"] for post in body.findAll("tr", {"class": "athing"})]
    discussions = []
    for i in ids:
        discussions.append(body.findAll("span", {"id": f"unv_{i}"})[0].findNext("a", {"href": f"item?id={i}"}).text)
    comments = []
    for word in discussions:
        comments.append(int(word.split()[0]) if not word.isalpha() else 0)
    titles = [title.text for title in body.findAll("a", {"class": "titlelink"})]
    news_list = []
    for i, _ in enumerate(titles):
        news_list.append(
            {
                "author": authors[i],
                "comments": comments[i],
                "points": points[i],
                "title": titles[i],
                "url": urls[i],
            }
        )
    return news_list


def extract_next_page(parser):
    """Extract next page URL"""
    body = parser.findAll('table')[2]
    return body.findAll("a", {"class": "morelink"})[0]["href"]


def get_news(url, n_pages=1):
    """ Collect news from a given web page """
    news = []
    while n_pages:
        print("Collecting data from page: {}".format(url))
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        news_list = extract_news(soup)
        next_page = extract_next_page(soup)
        url = domain + next_page
        news.extend(news_list)
        n_pages -= 1
    return news


if __name__ == "__main__":
    print(get_news(domain + "front", n_pages=2)[:10])
