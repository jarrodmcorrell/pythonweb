from bs4 import BeautifulSoup
import requests
import re

url = 'https://www.ratemyarea.com'
data = requests.get(url)
f = open("places.txt","w")

soup = BeautifulSoup(data.text, 'html.parser')
#mydivs = soup.find_all("div", class_= "col-md-4 slab")
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

state_names = ["Alabama", "Alaska", "Arizona", "Arkansas", "California",
     "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", 
     "Iowa", "Kansas", "Kentucky", "Louisiana", 
     "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", 
     "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", 
     "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", 
     "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", 
     "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

for link in soup.find_all("div", class_="col-md-4 slab"):
    place = link.text.strip()
    if place == 'Washington Dc':
        f.write("Washington D.C.\n")
    else:
        lasttwo = place[-2:]
        ltwo = lasttwo.upper()
        index = states.index(ltwo)
        ltwo = state_names[index]
        removelasttwo = place[:-2]
        rmltwo = removelasttwo[:-1]
        f.write(rmltwo + ", " + ltwo + "\n")

f.close()
