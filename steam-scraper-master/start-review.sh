#!/usr/bin/sh
virtualenv -p python3.7 env
. env/bin/activate
pip install -r requirements.txt
scrapy crawl reviews -o reviews.jl -a url_file=re_url$1 -s JOBDIR=output/reviews
