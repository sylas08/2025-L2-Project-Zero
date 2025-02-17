# Functions go here
def string_check(question, valid_ans_list, num_letters):
    """Checks that users enter the full world
    or the 'n' letter/s of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire world
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


# Main Routine goes here
yes_no_list = ['yes', 'no']
payment_list = ['cash', 'credit']

like_coffee = string_check("Do you like coffee? ",
                           yes_no_list, 1)

print(f"You chose {like_coffee}")
pay_method = string_check("Payment_method: ", payment_list, 2)
print(f"You chose {pay_method}")
