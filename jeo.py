#!/usr/bin/python3
""" multiline comment goes here """
#Jeopardy game
# import a library to make an HTTP request

import requests

def main():
    # prompt for initials

    player = input("Type in your initials:")
    rounds = input("How many rounds you'd like to play?")
    #make a request to http://jservice.io/api/random
    resp =requests.get(f"http://jservice.io/api/random?count={rounds}")
    # strip off JSON from the 200 response
    listogquestions = resp.json()

    # run the game by looping over the results
    for question in listofquestions:
        print(f"Alex says:(question['question']}")
        playeranswer = input("\tType your answer-->")
        if playeranswer.lower() == question['answer'].lower(): print(f\Alex says: that's right, you add {jquestion['value']} to your score")


        print(question['question'])
        print
    # each time through 
    # according to the docs, ?count = 10 appended to the URI will return 10 results
    # run for 10 rounds by looping over the results



   # astroData = requests.get('http://api.open-notify.org/iss-now.json')
    #for data in astroData.json():
     #   print(data)
      #  print(astroData.json()[data])
   # issdata = astroData.json()

    #print(issdata["iss_position"]["latitude"])

if __name__ == '__main__':
    main()

