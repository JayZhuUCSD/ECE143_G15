# readme steam scraper for G15
This program was forked form [here](https://github.com/prncc/steam-scraper) so that we could pass the age verification on steam, and we did some modification to correct some small errors in this program and meet our requirements.
## start the program 
> Notice: The program can only be run on Linux or Mac OS.

* Download this project from github and unzip it.

* The python version of this is python 3.7, python 3.x is supported but you might need to do some modification at the begining of this project. I've written a scripts to realize one-step start, if you want to use another version of python, just change the first line of the python version. 
* Check your python version, run the subcripts
```bash
cd steam-scraper-master
bash ./start-game.sh
```

* e.g: The scripts to start the review scraper. 
```bash
#!/usr/bin/sh
virtualenv -p python3.7 env # set the pyhton version
. env/bin/activate
pip install -r requirements.txt
mkdir ./output
cd ./output
touch products_all.log
cd ..
scrapy crawl products -o output/products_all.jl --logfile=output/products_all.log --loglevel=INFO -s JOBDIR=output/products_all_job -s HTTPCACHE_ENABLED=False
```
* After doing this, we will get an output file contains all the games on steam in ./output/. To get their reviews, we need to first extract all the reviews' urls out.  Notice that this is very tricky to split the file into 10 pieces, for there are more than 10,000,000 comments on steam, you will definetily do not want to run a single thread to do this job, then getting ten scrapers working together would be a good choice.
```python
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 12:14:02 2018
Extrac all the reviews' urls from raw data file and 
@author: Fangzhou Ai
"""
fname='Products_all.jl'
f=open(fname,'r',encoding="utf8")


g1=open('re_url1','w')
g2=open('re_url2','w')
g3=open('re_url3','w')
g4=open('re_url4','w')
g5=open('re_url5','w')
g6=open('re_url6','w')
g7=open('re_url7','w')
g8=open('re_url8','w')
g9=open('re_url9','w')
g0=open('re_url0','w')
i=0
for line in f:
    exec('temp=%s'%line)
    try:
       assert int(str(temp['all_view']).replace(',',''))>0 #check if it has comments
    except AssertionError:
       continue
    try:
       assert temp['reviews_url'] #extract url
    except KeyError:
        continue
    a=temp['reviews_url']+'\n'
    exec('g%d.write(a)'%i)

    i=i+1
    i=i%10     

f.close()
g0.close()
g1.close()
g2.close()
g3.close()
g4.close()
g5.close()
g6.close()
g6.close()
g7.close()
g8.close()
g9.close()

print('done')
```
* So let's see what we have now, a raw data file in ./output and ten files contain the reviews' urls, my teammates will do further analysis to the raw data, but let's keep looking for more information.

* Find a large disk and create ten folders, unzip the project to each file, which means we have ten scrapers now. We could give these folders a number like steam-scraper-master0/ to  steam-scraper-master9/, then we copy the reviews' urls to each folder according to their own number, from re_url0 to re_url9.

* Enter each folder, run the review script.
* eg, for steam-scraper-master4
 ```bash
 cd steam-scraper-master4
 bash start-review.sh 4 #remenber to input your folder's number
 ```
 * The start-review.sh
```bash
#!/usr/bin/sh
virtualenv -p python3.7 env # set the pyhton version
. env/bin/activate
pip install -r requirements.txt
scrapy crawl reviews -o reviews$1.jl -a url_file=re_url$1 -s JOBDIR=output/reviews
```
* You could start ten scrapers at teh same time, but make suer you have a good connectivity to Internet and a stable and powerful PC!

## Structure of scraper.

* This project mainly use the module [scrapy](https://scrapy.org/) to fetch the information from internet, also use some simple module like [re](https://docs.python.org/3/library/re.html) to find the keyword.

* The most two important file to us is ./steam-scrapersteam/items.py and ./steam-scraper/steam/spiders/product_spider.py, the former one define the data structure how we store the information, the latter one tell us how to get these onformation.

### items.py
* This is the original data structure
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
* In the original program the n_reviews tag cannot work so I delete it, what's more, to know better about how many people have left their comments and wether they are positive, I add four tags, all_reviewn, all_ratio, recent_review, recent_ratio, means the number of all the comments and the positive/all ratio, the number of  recent 30 days' comments and the positive/all ratio. I also add the platform as the variable to get more details.
```python
    recent_ratio=scrapy.Field()
    all_ratio=scrapy.Field()
    platform=scrapy.Field()
    recent_view = scrapy.Field()
    all_view = scrapy.Field()
```
* All these data structure are stored in class ProductItem(scrapy.item), it's obvious that this class inherit from scrapy.

###  product_spider.py
* This file describe how we get those information defined in items.py. There are sevral methods to acquire information.

* Regular matching expression
```python
    for i in plat:
        if re.findall(r'Windows',i) or re.findall(r'win',i):
            platform.append("Windows")
        if re.findall(r'Mac',i) or re.findall(r'mac',i):
            platform.append("Mac")
        if re.findall(r'Linux',i) or re.findall(r'linux',i):
            platform.append("Linux")
        if re.findall(r"SteamOS",i):
            platform.append('SteamOS')
```
* css style match
```python
reviewers = response.css('.responsive_hidden').extract()
    if len(reviewers)==0:
        all_view=0
        recent_view=0#
        loader.add_value('all_view',all_view)
        loader.add_value('recent_view',recent_view)
    elif len(reviewers)==1:
        recent_view=0
        loader.add_value('recent_view', recent_view)
        if re.findall(r"\(([\d,]+)\)",reviewers[0]):
            all_view=re.findall(r"\(([\d,]+)\)",reviewers[0])
        else:
            all_view=-1
        loader.add_value('all_view', all_view)
    elif len(reviewers)==2:
        if re.findall(r"\(([\d,]+)\)",reviewers[0]):
            recent_view=re.findall(r"\(([\d,]+)\)",reviewers[0])
        else:
            recent_view=-1
        loader.add_value('recent_view', recent_view)
        if re.findall(r"\(([\d,]+)\)",reviewers[1]):
            all_view=re.findall(r"\(([\d,]+)\)",reviewers[1])
        else:
            all_view=-1
        loader.add_value('all_view', all_view)
    else:
        all_view = -1
        recent_view = -1
        loader.add_value('all_view', all_view)
        loader.add_value('recent_view', recent_view)price = response.css('.game_purchase_price ::text').extract_first()
```
## Age verification
* When a game need an age verification, the web will call the age.app, if we detect this we will send the age information below to the age.app to avoid this
```python
        if '/agecheck/app' in response.url:
            logger.debug(f'Form-type age check triggered for {response.url}.')

            form = response.css('#agegate_box form')

            action = form.xpath('@action').extract_first()
            name = form.xpath('input/@name').extract_first()
            value = form.xpath('input/@value').extract_first()

            formdata = {
                name: value,
                'ageDay': '1',
                'ageMonth': '1',
                'ageYear': '1955'
            }
```

