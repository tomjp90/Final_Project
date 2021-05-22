from bs4 import BeautifulSoup as bs
import requests
import os
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys
from datetime import datetime

#------------------------------------------------------
def scrape_house_listing(url):
      # load chrome driver and browser for scraping
      executable_path = {'executable_path': "chromedriver.exe"}
      browser =  Browser("chrome", **executable_path, headless=False)
      
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
            # visit url and save html
            response = requests.get(url)
            browser.visit(url)
            html = browser.html
            soup = bs(html, 'html.parser')
            browser.quit()  

            try:
                  # find and store relevant html
                  summary = soup.find("div", class_="css-fpm9y")
                  property_features = summary.find_all('span', class_='css-1rzse3v')
                  
                  # extract property features
                  bedrooms = property_features[0].text.split(' ')[0]
                  bathrooms = property_features[1].text.split(' ')[0]  

                  # try and catch when features cannot be scraped
                  try:
                        cars = property_features[2].text.split(' ')[0] 
                  except:
                        cars = "Unknown"
                  try:
                        landsize = property_features[3].text.split(' ')[0][:-2]
                  except:
                        landsize = "Unknown"                  
                  try:
                        property_type = summary.find('span', class_='css-in3yi3').text
                  except:
                        property_type = "Unknown" 

                  # find address from property features
                  address = summary.find('h1', class_='css-164r41r').text
                  postcode = address.split(' ')[-1]
                  state = address.split(' ')[-2]       

                  # split address around suburb to extract one or two worded suburbs
                  street_types = ["street","Street","avenue","Avenue","road","Road","st","St","Rd"]
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
                  property_img = soup.find("picture", class_="css-8yo374").find("source")['srcset']            
                  
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
                        "future_predict": []                        
                        }

      # results if scraping failed
            except:

                  house_features = "error"        
      
      except:
            browser.quit()
            house_features = "Invalid URL"

      # return dictionary of features
      return house_features
