from splinter import Browser
import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
import pandas as pd

#taken from activity #9 Day 3
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


mars_web = {}
hemisphere_image_urls = []
# #news scrape
def scrape_news():
    
    browser = init_browser()
    
    #Launches Website
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    html=browser.html

    #### Sets up the Necessary Variables for the Most Recent News Article.
    #need to get a variable for 'news_title' and 'news_p'
    soup = bs(html, 'html.parser')
    latest_news_date = (soup.find_all('div', class_="list_date"))[0].get_text()
    latest_news_title = (soup.find_all('div', class_='content_title'))[0].get_text()
    latest_news_paragraph = (soup.find_all('div', class_='article_teaser_body'))[0].get_text()
    
    mars_web['latest_news_date'] = latest_news_date
    mars_web['latest_news_title'] = latest_news_title
    mars_web['latest_news_paragraph'] = latest_news_paragraph
   
    browser.quit()
    return mars_web
    
def scrape_marsImg():
    browser = init_browser()
    #### Set up Scraper for Mars Images from Images Site.
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html=browser.html
    soup = bs(html, 'html.parser')
    #need to scrape for featured image url, variable featured_image_url
    image = (soup.find_all('div', class_='carousel_items')[0].a.get('data-fancybox-href'))
    #example of print out
    featured = 'https://www.jpl.nasa.gov'+ image
    
    mars_web['featured_image'] = featured
    
    browser.quit()
    return mars_web
    
def scrape_marsTwitter():
    browser = init_browser()
    #### Scrape Mars Weather From Twitter Account
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    html=browser.html
    soup = bs(html, 'html.parser')
    #Save The Tweet of the most Recent Mars Weather String.
    mars_weather = (soup.find_all('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')[0].get_text())
    
    mars_web['mars_weather'] = mars_weather
    
    browser.quit()      
    return mars_web
    
def scrape_marsFacts():
    browser = init_browser()
    ## Scraping Mars Facts Webpage
    url = 'https://space-facts.com/mars/'
    browser.visit(url)
    html=browser.html
    soup = bs(html, 'html.parser')
    tables_df = ((pd.read_html(url))[0]).rename(columns={0: "Attribute", 1: "Value"}).set_index(['Attribute'])
    html_table = (tables_df.to_html()).replace('\n', '')
    
    mars_web['mars_data'] = html_table
    browser.quit()
    return mars_web
        
def scrape_marsHemi1():
    browser = init_browser()
    ### Mars Hemispheres Scraping
    #cerberus url
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url)
    html=browser.html
    soup = bs(html, 'html.parser')
    cerberus_url = (soup.find_all('div', class_='downloads')[0].li.a.get('href'))
    mars_web['hemisphere_urls'] = hemisphere_image_urls
    hemisphere_image_urls.append([{"title": "Cerberus Hemisphere", "img_url": cerberus_url}])
    
    browser.quit()
    return mars_web
    
def scrape_marsHemi2():
    #scrape
    #Schiaparelli Hemisphere url
    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url)
    html=browser.html
    soup = bs(html, 'html.parser')
    schiaparelli_url = (soup.find_all('div', class_='downloads')[0].li.a.get('href'))
    hemisphere_image_urls.append([{"title": "Schiaparelli Hemisphere", "img_url": schiaparelli_url}])

    browser.quit()
    return mars_web
    
def scrape_marsHemi3():        
    #scrape
    #Syrtis Major Hemisphere
    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url)
    html=browser.html
    soup = bs(html, 'html.parser')
    syrtis_major_url = (soup.find_all('div', class_='downloads')[0].li.a.get('href'))
    hemisphere_image_urls.append([{"title": "Syrtis Major Hemisphere", "img_url": syrtis_major_url}])

    browser.quit()
    return mars_web
        
def scrape_marsHemi4():     
    #scrape
    #Valles Marineris Hemisphere Url
    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url)
    html=browser.html
    soup = bs(html, 'html.parser')
    valles_marineries_url= (soup.find_all('div', class_='downloads')[0].li.a.get('href'))
    hemisphere_image_urls.append([{"title": "Valles Marineris Hemisphere", "img_url": valles_marineries_url}])

    browser.quit()
    return mars_web