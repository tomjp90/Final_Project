# Melbourne Price Predictor 

This project utilises Machine Learning to predict Melbourne property prices. It provides a simple resource for prospective property buyers to value listings they have found on Domain.com.au.  The web app scrapes property information from a provided Domain URL, appending crime and location information to the scraped data. The model then predicts a value for the property based on the listing information it receives.

## Heroku deployment

The project has been deployed to Heroku and is available [here](https://melbpricepredictor.herokuapp.com/)

## The Team 

- Catherine Sloan: https://github.com/catherinesloan
- Danielle Cahill: https://github.com/dan1ellec
- Anne Wieggers: https://github.com/annewieggers
- Tom Peddlesden: https://github.com/tomjp90 
- Joe Quinn: https://github.com/joeq94

## Data sources 

- [Melbourne Housing Data](https://www.kaggle.com/anthonypino/melbourne-housing-market?select=Melbourne_housing_FULL.csv)

- [Victorian Crime Data](https://discover.data.vic.gov.au/dataset/crime-by-location-data-table)


## Libraries and Technologies 

Machine Learning
-  XGBoost
- Scikit-learn
- Pandas
- Joblib

Back End
- Flask
- Flask PyMongo
- Numpy	
- scrape_mars
- requests
- BeautifulSoup 
- Selenium
- OS
- Splinter
- ChromeDriverManager
- Time
- Sys

Front end
- HTML
- CSS
- Javascript
- Bootstrap


## The Model

The XGBRegressor model from the XGBoost library was utilised for this project. Two versions of the model were created to accomodate the variation in property information included on Domain.

Model 1 was trained on the following features:
1. Number of Bedrooms
2. Number of Bathrooms
3. Number of Car Spaces
4. Property Type (Unit, Townhouse, House)
5. Year of sale
6. Month of sale
7. Suburb Crime Rate
8. Distance from CBD
9. Land Size

Model 2 was trained on the following features:
1. Number of Bedrooms
2. Number of Bathrooms
3. Number of Car Spaces
4. Property Type (Unit, Townhouse, House)
5. Year of sale
6. Month of sale
7. Suburb Crime Rate
8. Distance from CBD

## Overview repository

## Steps

1. Retrieving training dataset
- Data cleaning (such as dropping non relevant columns and null values, merging dataframes)

2. Retrieving testing data through scraping 
- Retrieve page with ChromeDriverManager and get URL
- Parse URL into BeautifulSoup to scrape data
- Initialise browser / return house features

3. Create Flask app to create routes to the relevant data points used
- Creating routes for index.html
	- Route to render index.html
	- Route to trigger the scrape function (parse in Domain URL and scrape info from website)

4. Setting up model 
- Using XG Boost in order to train and test the model
	- read in csvs
	- correlation matrix
	- assign data to x and y values
	- convert categorial data (suburbs) to numbers through one-hot encoding/get_dummies
	- scaling and normalisation
	- fit the model to the scaled training data and make predictions using the scaled test data

5. Prepare web page 
-	About page with prediction app
-	Team and skills page
-	Data page

6. Heroku deployment

## Caveats
-	Dropped columns that had nulls/NAs. 
-	Bedrooms 2 came from other source to ignored and used number of rooms instead
-	What date to scrape and pass in to the model for the prediction. Not all listings are auctions so we don’t know the date that they will sell. Using the date the prediction is made instead. 


## Challenges and potential improvements

Challenges encountered:
- 	Data availability (limited to Melbourne and 2016-2018 only)
- 	Linear regression wasn't a suitable approach for ML (negative R2 values) so other options had to be 
-	Domain.com.au blocks web scraping through BeautifulSoup

Potential improvements:
- 	More recent data to make a more accurate model
- 	Extending the app to predict from other resources such as realestate.com
- 	The opportunity to compare multiple houses on the website

