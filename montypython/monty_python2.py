#!/usr/bin/env python3


def main():
    """
    round = 0
    while True:
        round = round + 1
        print('Finish the movie title, "Monty Python\'s The Life of ______"')
        answer = input("Your guess--> ")
    if answer == 'Brian':
           print('Correct')
           break
    elif round == 3:    # logic to ensure round has not yet reached 3
             int('Sorry, the answer was Brian.')
           break             # break statement escapes the while loop
    else:                 # if answer was wrong, and round is not yet equal to 3
          print('Sorry. Try again!')

    """


round = 0
answer = " "
while round < 3 and answer != "Brian":
    round += 1     # increase the round counter by 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
    if answer == "Brian": # logic to check if user gave correct answer
        print("Correct!")
    elif round == 3:    # logic to ensure round has not yet reached 3
        print("Sorry, the answer was Brian.")
    else:                 # if answer was wrong
        print("Sorry. Try again!") 
    if __name__ == "__main__":
        main()        
