calculation_to_hours = 24
name_of_unit = "hours"


def days_to_units(number_of_days):
    return f"{number_of_days} days are {number_of_days * calculation_to_hours} {name_of_unit}"


def validate_and_execute():
    try:
        user_input_number = int(numbers_of_days_element)

        # we want to do conversion only for positive integers
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a valid positive number")
        else:
            print("you entered a negative number, no conversion for you")
    except ValueError:
        print("your input is not a valid number, don't ruin my program!")


user_input = ""
while user_input != "exit":
    user_input = input("Enter number of days as a comma separated list and I will convert it to hours! Or exit to exit\n")
    for numbers_of_days_element in user_input.split(","):
        validate_and_execute()
