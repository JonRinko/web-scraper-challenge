#pip install Flask_PyMongo 

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars = mars)
    
@app.route("/scrape")
def scraper():
    # listings = mongo.db.listings
    # listings_data = scrape_craigslist.scrape()
    
    mars = mongo.db.mars
    mars_web = scrape_mars.scrape_news()
    mars_web = scrape_mars.scrape_marsImg()
    mars_web = scrape_mars.scrape_marsTwitter()
    mars_web = scrape_mars.scrape_marsFacts()
    mars_web = scrape_mars.scrape_marsHemi1()
    mars_web = scrape_mars.scrape_marsHemi2()
    mars_web = scrape_mars.scrape_marsHemi3()
    mars_web = scrape_mars.scrape_marsHemi4()
    
    mars.update({}, mars_web, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)