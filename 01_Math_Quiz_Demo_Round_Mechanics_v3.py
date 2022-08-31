import random

#Function go here
def yes_no(question):
    valid = False
    while not valid:
        respones = input(question).lower()

        if respones == "yes" or respones  == "y":
            return "yes"


        elif respones == "no" or  respones == "n":
            return "no"


        else:
            print ("Please anwser yes / no ")


def instructions():

    print("**** How to Play ****")
    print()
    print("*THE INSTRUCTIONS OF THE QUIZ*")
    print()
    print("You will be asked how much question you would like")
    print("Next you will have to answer the number of question,")
    print("you have asked for or type 'xxx' for infinite mode.")
    return ""


def num_check(question, low, high):
    error = "Please enter an whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amoun tis too low / too high give
            if low < response <= high:
               return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)


def statement_generator(statement, decoratoin):

    side = decoratoin * 3

    statement = "{} {} {}".format(side, statement, side)
    top_bottom = decoratoin * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main Routine goes here...
statement_generator("Welcome To My MATHS QUIZ", "*")
print()


played_before = yes_no("Have you played the game before? ")

if played_before == "no":
   instructions()

print()

# Ask user how much they want to play with...
how_much = num_check("How much would questions "
                     "would you like? ", 0, 10)

balance = how_much

rounds_played = 0 

play_again = input("Press <Enter> to play...") .lower()
while play_again == "":

    #increase # of rounds played
    rounds_played += 1
