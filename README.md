# WebCrawler
This is a simple web crawler which fetches URLs using Python's multiprocessing ThreadPool library.

## Setup

Note: I developed this program in a Python 3.9.0 pyenv environment on MacOS Big Sur.

`pip install -r requirements.txt`

## Run

| Option     | Type   | Description                                        |
|------------|--------|----------------------------------------------------|
| --base_url | String | Base url of website to start crawler at [required] |
| --limit    | Int    | Number of pages to process                         |
| --threads  | Int    | Number of threads for parallel processing          |
| --help     |        | Show this message and exit.                        |

Example basic execution:  
`python3 crawler.py --base_url="https://www.pdx.edu"`

Example run with custom limit and/or threads:  
`python3 crawler.py --base_url="https://www.pdx.edu" --limit=30 --threads=10`

For help:  
`python3 crawler.py --help`

## Testing

I used the Python unittest library with Click.testing to test the multiprocessing feature.

To run the test:  
`python3 -m unittest test_crawler.py`





