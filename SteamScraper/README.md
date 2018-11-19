# SteamScraper

This repository contains [Scrapy](https://github.com/scrapy/scrapy) spiders for **crawling products** and **scraping all user-submitted reviews** from the [Steam game store](https://steampowered.com).
A few scripts for more easily managing and deploying the spiders are included as well.

This repository contains code accompanying the *Scraping the Steam Game Store* article published on the [Scrapinghub blog](https://blog.scrapinghub.com/2017/07/07/scraping-the-steam-game-store-with-scrapy/) and the [Intoli blog](https://intoli.com/blog/steam-scraper/).

Also, this repository contains the tutorial from [prncc github](https://github.com/prncc/steam-scraper.git) 

## Installation

After cloning the repository with
```bash
git clone https://github.com/JayZhuUCSD/ECE_G15.git
```
start and activate a Python 3.7 virtualenv with
```bash
cd ECE_G15/SteamScraper
virtualenv -p python3.7 env
. env/bin/activate
```
Install Python requirements via:
```bash
pip install -r requirements.txt
```
Before runing the code, please create the output file
```bash
mkdir ./output
cd output
touch products_all.log
cd ..
```

## Crawling the Products

The purpose of `ProductSpider` is to discover product pages on the [Steam product listing](http://store.steampowered.com/search/?sort_by=Released_DESC) and extract useful metadata from them.
A neat feature of this spider is that it automatically navigates through Steam's age verification checkpoints.
You can initiate the multi-hour crawl with
```bash
scrapy crawl products -o output/products_all.csv --logfile=output/products_all.log --loglevel=INFO -s JOBDIR=output/products_all_job -s HTTPCACHE_ENABLED=False
```
When it completes you should have metadata for all games on Steam in `output/products_all.jl`.
Here's some example output:
```python
{
  'app_name': 'Cold Fear™',
  'developer': 'Darkworks',
  'early_access': False,
  'genres': ['Action'],
  'id': '15270',
  'metascore': 66,
  'n_reviews': 172,
  'price': 9.99,
  'publisher': 'Ubisoft',
  'release_date': '2005-03-28',
  'reviews_url': 'http://steamcommunity.com/app/15270/reviews/?browsefilter=mostrecent&p=1',
  'sentiment': 'Very Positive',
  'specs': ['Single-player'],
  'tags': ['Horror', 'Action', 'Survival Horror', 'Zombies', 'Third Person', 'Third-Person Shooter'],
  'title': 'Cold Fear™',
  'url': 'http://store.steampowered.com/app/15270/Cold_Fear/'
 }
```
