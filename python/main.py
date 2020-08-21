#title: magleads dbm
#version: 0.01
#idea: uses google places api to find businesses near location specified
#goal: poors into database after user review
#creator: jarrod correll

from bs4 import BeautifulSoup
import requests
from os import system
import googlemaps
import pprint
import time
import requests,json

API_KEY = 'AIzaSyA9kukEGExnGpRUomg3k98YKs_wdkUM4Qw'
gmaps = googlemaps.Client(key = API_KEY)

def gmapsfind(loc,genre):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    r = requests.get(url + 'query=' + genre+"in"+loc + "&key=" + API_KEY)
    x = r.json()
    y = x['results']
    
    z = x['next_page_token']
    number = 0

    for i in range(len(y)):
        #print(y[i])
        print("Name: " + y[i]['name'])
        print("Type: " + genre)
        print("Location: " + y[i]['formatted_address'])
        print("Place Id: " + y[i]['place_id'])
        print("Phone #: " + getPhone(y[i]['place_id']))
        print("Website: " + getWebsite(y[i]['place_id']))
        number = number+1

    if number==20:
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json?pagetoken="
        r = requests.get(url+z+"&key=" + API_KEY)
        a = r.json()
        b = a['results']

        c = a['next_page_token']

        for i in range(len(b)):
            print("Name: " + b[i]['name'])
            print("Type: " + genre)
            print("Location: " + b[i]['formatted_address'])
            print("Place Id: " + b[i]['place_id'])
            print("Phone #: " + getPhone(b[i]['place_id']))
            print("Website: " + getWebsite(b[i]['place_id']))
            number = number+1

        if number == 40:
            url = "https://maps.googleapis.com/maps/api/place/textsearch/json?pagetoken="
            r = requests.get(url+c+"&key=" + API_KEY)
            d = r.json()
            e = d['results']

            for i in range(len(e)):
                print("Name: " + e[i]['name'])
                print("Type: " + genre)
                print("Location: " + e[i]['formatted_address'])
                print("Place Id: " + e[i]['place_id'])
                print("Phone #: " + getPhone(e[i]['place_id']))
                print("Website: " + getWebsite(e[i]['place_id']))
                number = number+1
        else:
            print("No third page")
    else:
        print("No second page")
    
    print("" + str(number) + " result(s) for " + genre + "s in "+ loc)
    

def getWebsite(placeid):
    url = "https://maps.googleapis.com/maps/api/place/details/json?place_id="+placeid+"&fields=website&key="+API_KEY
    r = requests.get(url)
    x=r.json()
    y=x['result']
    try:
        return y['website']
    except:
        return ""

def getEmail():
    email = ""
    return email

def getPhone(placeid):
    url = "https://maps.googleapis.com/maps/api/place/details/json?place_id="+placeid+"&fields=formatted_phone_number&key="+API_KEY
    r = requests.get(url)
    x=r.json()
    y=x['result']
    try:
        return y['formatted_phone_number']
    except:
        return ""

def yelpfind(loc,genre):
    print("yelpyelpyelp")

system('cls')
print("magleads dbm --version 0.01")
print("commands: ")
print("<add>: adds new entries, takes parameters type and location")
print("<edit>: edit entries in the database")
print("<quit>: exits the dbm")

a = 1

while(a==1):
    command = input("$:")
    if command == "add":
        l = input("location: ")
        t = input("type: ")
        gmapsfind(l, t)
    elif command == "edit":
        print("edit command")
    elif command == "quit":
        print("bye bye")
        a=2
        break;
    else:
        print("invalid command")

print("...done")




