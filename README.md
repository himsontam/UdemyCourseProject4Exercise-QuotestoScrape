# UdemyCourseProject4Exercise-QuotestoScrape
This is a Udemy tutorial to learn Scrapy. Modern Web Scraping with Python using Scrapy Splash Selenium

Link to scrapy: http://books.toscrape.com/

# Scrapy command:
- run scrapy script -----> scrapy crawl quotes

- run scrapy shell ------> scrapy shell

- Create New Scrpay Project -------> scrapy startproject QuotestoScrape

- You can start your first spider with:
  - cd QuotestoScrape
  - scrapy genspider example example.com

- Create Scrapy spider -------> scrapy genspider quotes http://quotes.toscrape.com/js/

- Create Scrapy spider with template -------> scrapy genspider -t crawl quotes http://quotes.toscrape.com/js/

- scrapy genspider -l
  - Available templates: basic, crawl, csvfeed, xmlfeed

- Export Excel Command -----> scrapy crawl quotes -o quotes.csv

- Export JSON Command ------> scrapy crawl quotes -o quotes.json

# Anaconda command:
- install dependencies ----> conda install -c conda-forge scrapy==1.6 pylint autopep8 -y
- install iPython ---------> conda install iPython

# docker command
- docker run [containerID] ---------> run the existing docker contianer image
- docker run it -p 8050:8050 scrapinghub/splash -------> run the docker splash command
- docker ps -------> check running container image
- docer ps -a -----> check all existing continaer image


- http://localhost:8050/ -----> check splash docker loalhost website
