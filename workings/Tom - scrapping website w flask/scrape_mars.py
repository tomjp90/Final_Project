from bs4 import BeautifulSoup as bs
import requests
import os
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time


#def initialise_browser():
#    executable_path = {'executable_path': ChromeDriverManager().install()}
#    return Browser("chrome", **executable_path, headless=False)

#------------------------------------------------------
def scrape_news():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser =  Browser("chrome", **executable_path, headless=False)

    url = "https://mars.nasa.gov/news/"
    response = requests.get(url)
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    #get first slide with latest news
    slides = soup.find('li', class_ = 'slide')
    content_title = slides.find('div', class_ = 'content_title').find('a').text.strip()
    article_teaser = slides.find('div', class_='article_teaser_body').text.strip()
    
    news_t_p = {"Title": content_title, 
                "Paragraph": article_teaser
                }

    browser.quit()
    return news_t_p
#------------------------------------------------------
def scrape_featured_image():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser =  Browser("chrome", **executable_path, headless=False)

    jpl_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    response = requests.get(jpl_url)
    browser.visit(jpl_url)
    html = browser.html
    soup = bs(html, 'html.parser')

    img = soup.find('div', class_ = 'header')
    img_link = img.find('img', class_='headerimage')['src']
    featured_image_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_link}'

    browser.quit()
    return featured_image_url


#------------------------------------------------------
def scrape_facts():
    table = pd.read_html('https://space-facts.com/mars/')
    facts_table = table[0]
    facts_table.columns = ['Description','Mars']
    facts_table = facts_table.set_index("Description")
    facts_html = facts_table.to_html(index=False)
    return facts_html

#------------------------------------------------------
def scrape_hemi_img():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser =  Browser("chrome", **executable_path, headless=False)

    hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    response = requests.get(hemi_url)
    browser.visit(hemi_url)
    html = browser.html
    soup = bs(html, 'html.parser')
    products = soup.find_all('div', class_='description')

    hemisheres = []
    for product in products:
        hemi = product.find('h3').text
        hemi_name = hemi.split(" Enhanced")[0]
        hemisheres.append(hemi_name)

    hemisphere_image_urls = []
    for hemisphere in hemisheres:
        browser.click_link_by_partial_text(f"{hemisphere}")
        html = browser.html
        soup = bs(html, "html.parser")
        img_url = (soup.find('div', class_="downloads").find('a')['href'])

        hemisphere_image_urls.append({"title": hemisphere, 
                                        "img_url":img_url
                                        })
        time.sleep(1)
        browser.back()

    browser.quit()

    return hemisphere_image_urls
