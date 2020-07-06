#!/usr/bin/python3
import requests

# import json

def main():

    astroData = requests.get('http://api.open-notify.org/iss-now.json') 
    for data in astroData.json():
        print(data)
        print(astroData.json()[data])
    issdata = astroData.json()

    print(issdata["iss_position"]["latitude"])

if __name__ == '__main__':
    main()

