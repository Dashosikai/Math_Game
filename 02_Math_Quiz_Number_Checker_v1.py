# Function go here
def number_checker(question):
    while True:
        response = input(question)

        round_error = "Please tytpe either <enter> or an " \
                      "or an integer that is more than 0\n"

        # If infinite mode not chosen, check response
        # is an integer that is more than 0
        if response != "":
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

#  **** Main Routine ******
user_answer = number_checker("What is 4 + 5? ")
print("you said", user_answer)