def intcheck(question, low=None, high=None, exit_code = None):

    while True:

        # sets up error messages
        if low is not None and high is not None:
            error = "Please enter an integer between {} and {} (inclusive)"
        elif low is not None and high is None:
            error = "Please enter an integer that is more than or equal to {}"
        elif low is None and high is not None:
            error = "Please enter an integer that is less than or equal to {}"
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
rounds = intcheck("how many questions would you like or press <enter> to chose infinite mode...", 1, exit_code = "")

if rounds == "":
    print("you chose infinite mode")
else:
    print("you asked for {} qusetions".format(rounds))

