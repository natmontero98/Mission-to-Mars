from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import Scraping

# Set up Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#  define the route for the HTML page (homepage)
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

# define the scraping route
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars    #variable that points to our mongo db
   mars_data = scraping.scrape_all()    #new variable to hold the newly scraped data (referencing scraping.py file)
   mars.update({}, mars_data, upsert=True) #update the db (insert the data)
   return redirect('/', code=302)   #navigate our page back to / to see updated content

if __name__ == "__main__":
   app.run()
