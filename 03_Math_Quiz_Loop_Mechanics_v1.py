# Function go here
def number_checker(question):
    while True:
        response = input(question)

        round_error = "Please tytpe either <enter> or an " \
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

how_many = number_checker("How many questions? Type 'xxx' for infinite")

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

