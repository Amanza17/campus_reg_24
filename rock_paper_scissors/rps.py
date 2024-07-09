import random

PC_CHOOSE = ['Rock', 'Paper', 'Scissors']
USR_CHOOSE = ['R', 'P', 'S']

def sayHello():
    #this function shows a screen to the player with the rules of the game
    print("Welcome to the game Rock Paper Scissors")
    print("These are the rules:")
    print("You have to write R for Rock, P for Paper and S for Scissors \n The computer will choose a random choice,"
          "and will automatically calculate the winner. Rock beats Scissors, Scissors beats Paper and Paper beats Rock")
    print("The winner will get one point, in case of tie neither player nor computer will get the point. The one who "
          "first reaches 3 points will be the winner of the game.")

def askForName():
    #this function gets the user name
    n = input("Now the rules havee been exxplained, tell me, what's your name? ")
    return n

def validate(n):
    #the function decides if the user choice is valid and translates it as needed
    if n in PC_CHOOSE:
        return n
    else:
        if n not in USR_CHOOSE:
            print("That's not a valid choice")
            return "E"

        if n == "R":
            return "Rock"
        if n == "P":
            return "Paper"
        if n == "S":
            return "Scissors"

def usrChoice():
    #this function gets the user choice
    n = input("Your choice is: ")
    n = validate(n)
    return n

def chooseRandom():
    #this fucntion randomly chooses rock paper or scissors for the computer
    return random.choice(PC_CHOOSE)


def compWin(computer,person):
    #this functoin is executed when the computer wins
    print("Computer wins! PC chose ", computer, "and you chose ", person)
    return "C"


def persWin(computer,person):
    #this functoin is executed when the user wins
    print("User wins! PC chose ", computer, "and you chose ", person)
    return "U"


def compare(computer, person):
    #this function decides who wins the game depending on their choices
    if computer == person:
        print("It's a tie! PC chose ", computer,  "and you chose ", person )
    elif computer == "Paper":
        if person == "Rock":
            return compWin(computer,person)
        if person == "Scissors":
            return persWin(computer, person)
    elif computer == "Rock":
        if person == "Paper":
            return persWin(computer, person)
        if person == "Scissors":
            return compWin(computer,person)

    elif computer == "Scissors":
        if person == "Rock":
            return persWin(computer, person)
        if person == "Paper":
            return compWin(computer,person)


def main():

    user_points = 0
    pc_points = 0

    sayHello()
    n = askForName()

    while ((user_points <3) and  (pc_points <3) ):
        comp = chooseRandom()
        per = usrChoice()
        if per != "E":
            res = compare(comp, per)
            if res == "U":
                user_points +=1
            if res == "C":
                pc_points +=1

            print ("The result in this moment is: User ", user_points, "and Computer ", pc_points)

    if (user_points == 3 ):
        print(n , " wins!")
    if (pc_points == 3 ):
        print("Computer wins!")




if __name__ == '__main__':
    main()