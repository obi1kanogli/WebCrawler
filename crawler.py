import requests
import re
import sys
from bs4 import BeautifulSoup

PAGES = []


def spider(url):
    page = requests.get(url)
    is_url = re.compile("^http")
    soup = BeautifulSoup(page.content, 'html.parser')
    print(url)
    for url in soup.find_all("a", href=is_url):
        if "href" in url.attrs:
            new_url = url.attrs["href"]
            print("  " + new_url)
            PAGES.append(new_url)


if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("error")
        exit(1)
    base_url = sys.argv[1]
    spider(base_url)
    while PAGES:
        spider(PAGES.pop(0))
