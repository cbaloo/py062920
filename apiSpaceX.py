#!/usr/bin/python3
"""
Author: RZFeeser
This program harvests SpaceX data avail from https://api.spacexdata.com/v3/cores using the Python Standard Library methods
"""

# using std library method for getting at API data
#import urllib.request 
#import json
# python3 -m pip install requests

import requests
# GOBAL / CONSTANT of the API we want to lookup
SPACEXURI = "https://api.spacexdata.com/v3/cores"

def main():
    # create a urllib.request response object by sending an HTTP GET to SPACEXURI
   # coreData = urllib.request.urlopen(SPACEXURI)
    coreData = requests.get(SPACEXURI)
    # pull STRING data off of the 200 response (even tho it's JSON!)
   # xString = coreData.read().decode()
   # print(type(xString))

    # convert STRING data into Python Lists and Dictionaries
   # listOfCores = json.loads(xString)
   
    listOfCores = coreData.json()

   # print(type(listOfCores))

    for core in listOfCores:
        print(core['core_serial'])
        print(core['original_launch'], end="\n\n")
        

if __name__ == "__main__":
    main()
