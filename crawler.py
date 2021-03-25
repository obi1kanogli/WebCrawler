import requests
import re
import click
from bs4 import BeautifulSoup
from time import time as timer
from multiprocessing.pool import ThreadPool

urls = []


def fetch_urls(url):
    """
    Fetches html content from URL and outputs all URLs within it
    :param url: URL of website page
    :return: None
    """
    page = requests.get(url)
    if page.status_code != 200:
        print(f"Incorrect status_code {page.status_code} for {url}")
        return
    is_url = re.compile("^http")
    soup = BeautifulSoup(page.content, 'html.parser')
    print(url)
    for url in soup.find_all("a", href=is_url):
        if "href" in url.attrs:
            new_url = url.attrs["href"]
            print(f"  {new_url}")
            urls.append(new_url)


@click.command()
@click.option('--base_url', required=True, help='Base url of website to start crawler at')
@click.option('--limit', default=100, help='Number of pages to process')
@click.option('--threads', default=20, help='Number of threads for parallel processing')
def main(base_url, limit, threads):
    start = timer()
    fetch_urls(base_url)
    ThreadPool(threads).map(fetch_urls, urls[:(limit - 1)])
    print(f"Elapsed Time: {timer() - start} for {limit} pages")


if __name__ == "__main__":
    main()
