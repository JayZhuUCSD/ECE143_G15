#!/bin/bash
pip install virtualenv
virtualenv -p python3.7 env
. env/bin/activate
pip install -r requirements.txt
cd ./output
cd ..
scrapy crawl products -o output/products_all.jl --logfile=output/products_all.log --loglevel=INFO -s JOBDIR=output/products_all_job -s HTTPCACHE_ENABLED=False
