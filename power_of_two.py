#!/usr/bin/env python3
# Created by: Santiago Hewett
# Created on: Nov 13, 2023
# This program will ask the user for a whole number
# and it will tell them the product
# from 0 to their number put the power of 2.


def main():
    # Get the user num as a string and display message about program

    print("This program will ask the user for a whole number and it ")
    print("will tell them the product ")
    print("from 0 to their number put the power of 2")
    user_num_string = input("Enter your integer: ")

    # initialize variables
    power = 1

    # Catch if the user num is something wrong

    try:
        # Convert user int as a string to int
        user_num_int = int(user_num_string)

        # Check if user num is negative
        if user_num_int < 0:
            print(
                "{} is a negative number, please enter a positive number".format(
                    user_num_int
                )
            )

        # loop for power of 2 of user_num_int

        else:
            for counter in range(user_num_int + 1):
                # calculation for the power of 2
                power = counter**2
                # display power
                print("{0} ^ 2 = {1}.".format(counter, power))

    # Display a message to the user if they entered something that is not valid

    except Exception:
        # Message for invalid user input
        print("\n{} is not a valid integer.".format(user_num_string))


if __name__ == "__main__":
    main()
