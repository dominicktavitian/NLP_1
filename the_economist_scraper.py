# Import Statements
import requests as r
import csv
import pandas as pd
import re
from bs4 import BeautifulSoup as bs


def scraper():

    # My CSV path
    csv_path = 'npr_rawData.csv'

    # Naming column headers
    column_title_row = ['author', 'published', 'title', 'text', 'site_url']

    # Starting URLs for the scrape
    starter_url = ['http://www.economist.com/news/europe/21730778-mutual-mistrust-between-two-administrations-scuppered-deal-avoid-head-clash']

    econ_page = r.get(starter_url)
    author_name = 'N/A' 
    # Creating a writer for the csv
    with open(csv_path, "w") as outfile:
        writer = csv.writer(outfile)

        # Writing the first column
        writer.writerow(column_title_row)

        # Looping through starting URL and appending a new number to the end
        for i in starter_url:
            # Grabbing the URL page
            econ_page = r.get(i.text.strip())

            # Grabbing only the html elements of the page
            econ_html = bs(econ_page.content, 'lxml')


            # Grabbing Name of title
            title_name = list(econ_page.find('span', class_='flytitle-and-title__title'))[0]


            # Body of articles
            body = clean_body_text(list(econ_page.find('div', class_='blog-post__text')))

            # grabbing date
            date = list(econ_page.find('time', class_= 'blog-post__datetime'))[0]
                    
            # Inputting list of ingredients into column unclean   
            row = []
            row.append(author_name)
            row.append(date)
            row.append(title_name)
            row.append(body)
            row.append(i)
            writer.writerow(row)


# Returns a list of ingredients in the recipe with the html tags stripped
# Takes in the ingredients with html tags
def get_author(author_name):
    author_name = list(author_name[1].children)
    return(author_name[0].strip())



def clean_body_text(body):
    bodied = ''
    body = body[6:]
    for sentence in body:
        cleanr = re.compile('<.*?>')
        bodied += " " + re.sub(cleanr, '', str(sentence))
    return(bodied)

# Calling the scraper method
scraper()


