def statement_generator(statement, decoration):


    side = decoration * 4

    statement = "{} {} {}".format(side, statement, side)
    
    top_bottom = "*" * len(statement)
    
    print(top_bottom)
    print(statement)
    print(top_bottom)

statement_generator("Welcome to my Math Quiz Game", "*")
print()
statement_generator("INSTRUCTIONS", "")
print()
statement_generator("You will be asked how much questions you would like.", "")
statement_generator("Next you will have to answer the number of qestions you have asked for", "")
statement_generator("you have asked for or type 'xxx' for infinite.", "")
print()

# Function go here
def number_checker(question):
    while True:
        response = input(question)

        round_error = "Please type either <enter> or an " \
                      "or an integer that is more than 0\n"

        # If infinite mode not chosen, check response
        # is an integer that is more than 0
        if response != "xxx":
            try:
                response = int(response)

                # If response is too low, go back to 
                # start of loop
                if response < 1:
                    print(round_error)
                    continue

            # If response
            except ValueError:
                print(round_error)
                continue

        return response


questions_asked = 0

how_many = number_checker("How many questions? Type 'xxx' for infinite ")

if how_many == "xxx":
    mode = "infinite"
    how_many = 10

else:
    mode = "regular"

while True:

    user_answer = number_checker("What is 4 + 5? ")
    print("you said", user_answer)

    questions_asked += 1

    if user_answer =="xxx" or questions_asked == how_many:
        break

    if mode == "infinite":
        how_many += 1

    # Headings!!

