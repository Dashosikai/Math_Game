



def intcheck(question, low=None, high=None, exit_code = None):


    while True:

        # sets up error messages
        if low is not None and high is not None:
            error = ""
        elif low is not None and high is None:
            error = ""
        elif low is None and high is not None:
            error = ""
        else:
            error = "Please enter an integer"

        try:
            response = input(question)
            
            # check to see if response is the exit code and return it
            if response == exit_code:
                return response
            
            # change the response into an integer
            else:
                response = int(response)

            # Checks response is not too low, not use of 'is not' keywords
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        # checks input is a integer
        except ValueError:
            print(error)
            continue

# ***** Main Routine ******
def statement_generator(statement, decoration):

    side = decoration * 4

    statement = "{} {} {}".format(side, statement, side)
    

    
    print(statement)
    

statement_generator("Welcome to my Math Quiz Game", "*")
print()
statement_generator("INSTRUCTIONS", "")
print()
statement_generator("You will be asked how much questions you would like.", "")
statement_generator("Next you will have to answer the number of qestions you have asked for.", "")
print()


# Ask user for # of rounds..
rounds = intcheck("How many questions would you like or press <enter> to chose infinite mode...", 1, exit_code = "")

def check_rounds():
    while True:
        response = intcheck("How many questions would you like or press <enter> to chose infinite mode...", 1, exit_code = "")

        round_error = "Please tytpe either <enter> " \
                      "or an integer that is more than 0"
        if response != "":
            try:
                response = int(rounds)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

            return response
            

# Main routine gose here...

rounds_played = 0
choose_instruction =()


# Ask user for # of rounds, <enter> for infinite mode 
rounds = check_rounds()
 

end_game = "no"
while end_game == "no":

     # Round Heading 
    print()
    if rounds == "":
         heading = "Continuous Mode: Round {}".format(rounds_played + 1)
         print(heading)
         choose = input("{} or 'xxx' to end: ".format(choose_instruction))
         if choose == "xxx":
             break
    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)
        print(heading)
        choose = input(choose_instruction)
        if rounds_played == rounds - 1:
             end_game = "yes"


    # rest of loop / game 
    print("You chose {}".format(choose))

    rounds_played += 1

print("Thank you for playing")
            