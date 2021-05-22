from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_scrape")

@app.route("/")
def home():
    text = 'Mission to Mars'

    return render_template("index.html", text = text)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_data = scrape_mars.scrape_news()

    title_paragraph = scrape_mars.scrape_news()
    featured_image_url = scrape_mars.scrape_featured_image()
    mars_facts_table = scrape_mars.scrape_facts()
    mars_hemi = scrape_mars.scrape_hemi_img()
   
    mars_news_data = {
        'news_title_p': title_paragraph,
        'featured_image_url': featured_image_url,
        'table':mars_facts_table,
        'hemisphere_image_urls': mars_hemi,
        }
        
    # update database
    mongo.db.collection.update({}, mars_news_data, upsert=True)
    mars_news_data = mongo.db.collection.find_one()

    return render_template("scrape.html", mars_news_data = mars_news_data)


if __name__ == "__main__":
    app.run(debug=True)
