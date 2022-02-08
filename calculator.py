# Welcome to 100 days of code day 10. I completed this project without the use
# of the udemy course. Therefore, my implementation is a bit different from what
# you would find on the course. However, the program works as intended without
# bugs so enjoy this python calculator

# Import logo
from logo_art import logo

# Welcome statement and logo print
print(logo)
print("Welcome to the calculator, lets get started!\n")

# Addition
def add(first_number, second_number):
    """Adds two given numbers together"""
    total = first_number + second_number
    return total

# Subtraction
def subtract(first_number, second_number):
    """Subtracts two given numbers"""
    total = first_number - second_number
    return total

# Multiplication
def multi(first_number, second_number):
    """Multiplies two given numbers together"""
    total = first_number * second_number
    return total

# Division
def division(first_number, second_number):
    """Divides two given numbers"""
    total = first_number / second_number
    return total

# Calculation function
def calculator():
    """Logic for choosing operation functions and playthrough"""

# Inputs for first number and initializing a play state
    first_number = float(input("Enter your first number\n"))
    playing = True

# while loop for play through
    while playing:
        operator = input("Choose your operator!\n +\n -\n *\n /\n")
        second_number = float(input("Enter your next number\n"))

# Choosing an operator logic
        if operator == "+":
            answer = add(first_number,second_number)
            print(f"{first_number} {operator} {second_number} = {answer}")
        elif operator == "-":
            answer = subtract(first_number,second_number)
            print(f"{first_number} {operator} {second_number} = {answer}")
        elif operator == "*":
            answer = multi(first_number,second_number)
            print(f"{first_number} {operator} {second_number} = {answer}")
        elif operator == "/":
            answer = division(first_number,second_number)
            print(f"{first_number} {operator} {second_number} = {answer}")

# Play again and use previous calculation logic
        calc_again = input(f"Would you like to continue calculating with {answer}?\n").lower()
        if calc_again == "yes":
            first_number = answer
        else:
            play_again = input("Would you like to perform another calculation?\n").lower()
            if play_again == "yes":
                calculator()
            else:
                playing = False

# Calling the function to start the actual calculation program
calculator()
