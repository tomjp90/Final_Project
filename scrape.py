from bs4 import BeautifulSoup as bs
import requests
import os
import pandas as pd
# from splinter import Browser
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
import time
import sys
from datetime import datetime
from selenium import webdriver
import numpy as np
# from selenium.webdriver.chrome.options import Options


#------------------------------------------------------
def scrape_house_listing(url):
      # load chrome driver and browser for scraping
      # executable_path = {'executable_path': "chromedriver.exe"}
      
      # check if domain or realestate website
      domain = 'domain'
      realestatate = 'realestate'

      # --------------------- CURRENT DATE---------------------------
      # get current day, month and year
      current_month = datetime.now().month
      current_year = datetime.now().year
      current_day =  datetime.now().day    
      
      # ------------------------ DOMAIN.COM.AU SCRAPE -----------------------------------
      try:
            # https://stackoverflow.com/questions/50831469/i-am-not-able-to-scrape-the-web-data-from-the-given-website-using-python        
            # prevent automation detection - create a 'valid user'
            # #----------------------------- RANDOMLY CREATE A 'USER' -------------------------------------------
            rand = np.random.randint(6)

            rand_headers0 = {'User-Agent': 'Chrome/6.1 (Mac; Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102',}
            rand_headers1 = {'User-Agent': 'Opera/8.4 (Macintosh; Mac OS X 10_11_6) Kit/538.36 (KHTML, like Gecko) Opera/50.1.3.54'}
            rand_headers2 = {'User-Agent': 'Chrome/5.1 (Windows; Win OS 10.3) WebKit/537.36 (HTML) Chrome/50.0.21.12'}
            rand_headers3 = {'User-Agent': 'Chrome/5.2 (Windows; Win OS 10.3) WebKit/537.36 (KHTML, like Gecko) Chrome/5012.0.21.12'}
            rand_headers4 = {'User-Agent': 'Chrome/5.1 (Windows; Win OS 10.3) WebKit/537.36 (like Gecko) Chrome/53.0.21.12'}
            rand_headers5 = {'User-Agent': 'Chrome/5.1 (Macintosh; Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102'}
            headers_list = [rand_headers0,rand_headers1,rand_headers2,rand_headers3,rand_headers4,rand_headers5]          
            headers = headers_list[rand]
            print(f'======================= THE RANDOM NUMBER {rand}')
            # headers = {
            #       'User-Agent': 'Chrome/5.0 (Macintosh; Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102'}
            print(headers)
            html_content = requests.get(url, headers=headers)
            html = html_content.text
            soup = bs(html, 'html.parser')
            
            # ---------------------------- FIND CLASS NAMES THAT CHANGE PERIODICALLY -----------------------------------
            address_class = soup.find(attrs={"data-testid": "listing-details__button-copy-wrapper"}).find("h1")["class"][0]
            pfeatures_class = soup.findAll("span", attrs={"data-testid": "property-features-feature"})[4]["class"][0]
            ptype_class = soup.find(attrs={"data-testid": "listing-summary-property-type"}).find("span")["class"][0]
            img_class = soup.find("picture")["class"][0]


            #-------------------------------------- SCRAPE PROPERTY FEATURES -------------------------------------------------
            property_features = soup.find_all('span', class_ = pfeatures_class)
            bedrooms = property_features[0].find(attrs={"data-testid": "property-features-text-container"}).text.split(' ')[0]
            bathrooms = property_features[1].find(attrs={"data-testid": "property-features-text-container"}).text.split(' ')[0]
            # try and catch when features cannot be scraped
            try:
                  cars = property_features[2].find(attrs={"data-testid": "property-features-text-container"}).text.split(' ')[0]
            except:
                  cars = "Unknown"
            try:
                  landsize = property_features[3].find(attrs={"data-testid": "property-features-text-container"}).text.split(' ')[0][:-2]
            except:
                  landsize = "Unknown"
            try:
                  property_type = soup.findAll('span', class_ = ptype_class)[1].text
            except:
                  property_type = "Unknown" 

            # find address from property features
            address = soup.find('h1', class_ = address_class).text
            postcode = address.split(' ')[-1]
            state = address.split(' ')[-2]       

            # split address around suburb to extract one or two worded suburbs
            street_types = ["street","Street","avenue","Avenue","Rd,", "rd,","road","Road","st","St","Rd"]
            state_names = ["VIC", "NSW", "QLD", "SA", "WA", "NT", "TAS", "ACT"]
            for t in street_types:
                  if t in address:
                        temp = address.split(f"{t} ")[1]                                
                        for state in state_names:
                              if state in temp:
                                    suburb = temp.split(f" {state}")[0]                                              
                                    break
                        break

            # find property feature image
            property_img = soup.find("picture", class_ = img_class).find("source")['srcset']            
            
            # pass all features to dictionary 
            house_features = {
                  "listing_url": url,
                  "bedrooms": bedrooms,
                  "bathrooms": bathrooms,
                  "cars": cars,
                  "landsize": landsize,
                  "image_url": property_img,
                  "address": address,
                  "ptype": property_type,
                  "postcode": postcode,
                  "state": state,
                  "suburb": suburb,
                  "day": current_day,
                  "month": current_month,
                  "year": current_year,
                  "prediction": [],
                  "melbourne_avg": [],
                  "suburb_distance_crime": [],
                  "predict_format": [],
                  "future_predict": [],
                  "future_predict_format": []                          
                  }

                  # results if scraping failed
            

                  # house_features = "error"        
      
      except Exception as e:
            driver.quit()
            house_features = ""

      # return dictionary of features
      return house_features
