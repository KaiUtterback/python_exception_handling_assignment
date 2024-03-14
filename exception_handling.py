# 1. Exceptional Weather Forecast

'''
Objective: The aim of this assignment is to enhance your understanding of exception handling by creating a weather forecast application that gracefully handles unexpected user input and provides user-friendly error messages.

Task 1: Start
Begin by setting up a simple user input loop that asks the user to enter the temperature in Fahrenheit.

Ensure that your program only accepts numerical input and provides a friendly error message if the user enters something that can't be converted to a number.

Task 2: Temperature Conversion
Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.

Use a try block to catch any potential errors during the conversion process, such as division by zero or overflow errors.

Task 3: User Experience
Implement an else block that prints the converted temperature in a user-friendly format.
Add a finally block that thanks the user for using the weather forecast application, ensuring that this message is displayed regardless of whether an exception was caught or not.
'''

def find_temp():
    while True:
        temp = input("Please enter the temperature in Fahrenheit: ")
    
        try:
            temp = int(temp)
        except ValueError:
            print("I'm sorry, please enter a number.")
            continue
 
        try:
            result_C = (temp - 32) * 0.556
            result_C = round(result_C, 2)
        except ZeroDivisionError:
            print("Error: Division by zero occurred.")
            continue
        except OverflowError:
            print("Error: Overflow occurred during calculation.")
            continue
        else:
            print(f"{temp} degrees Fahrenheit is equal to {result_C} degrees Celsius")
            break
        finally:
            print("Thank you for using the weather forecast application.")

# print()
# find_temp()

# 2. Calculator Concierge

'''
Objective: The aim of this assignment is to create a robust calculator program that can handle various mathematical operations and potential user input errors without crashing.

Task 1: Start
Set up a calculator that can perform addition, subtraction, multiplication, and division.

Prompt the user to select an operation and then request two numbers to perform the operation on.

Task 2: Operation Execution
For each operation, use a try block to execute the calculation and handle any exceptions that may occur, such as ZeroDivisionError for division operations.

Task 3: Polite Error Handling
In the except blocks, provide friendly error messages that guide the user on what went wrong and how to correct it.
Include an else block that displays the result of the calculation if everything went smoothly.
'''

def adds(add_nums):
    add_result = add_nums[0]
    for add in add_nums[1:]:
        add_result += add
    return add_result

def addition():
    print()
    add_nums = []
    while True:
        add_input = input("Enter a number to add or 'done' when finished: ")
        if add_input == 'done':
            break
        try:
            add = float(add_input)
            add_nums.append(add)
        except ValueError:
            print("Error: Please enter a valid number or 'done' to finish")

    if len(add_nums) < 2:
        print("Error: You need at least two numbers for addition")
    else:
        try:
            add_result = adds(add_nums)
            print(f"After adding\n {add_nums}\n your answer is {add_result}")
        except Exception as e:
            print(f"Error: An error occurred during addition - {e}")

def subtraction(sub_nums):
    sub_result = sub_nums[0]
    for sub in sub_nums[1:]:
        sub_result -= sub
    return sub_result

def subtract():
    print()
    sub_nums = []
    while True:
        sub_input = input("Enter a number to subtract or 'done' when finished: ")
        if sub_input == 'done':
            break
        try:
            sub = float(sub_input)
            sub_nums.append(sub)
        except ValueError:
            print("Error: Please enter a valid number or 'done' to finish")

    if len(sub_nums) < 2:
        print("Error: You need at least two numbers for subtraction")
    else:
        try:
            sub_result = subtraction(sub_nums)
            print(f"After subtracting\n {sub_nums}\n your answer is {sub_result}")
        except Exception as e:
            print(f"Error: An error occurred during subtraction - {e}")

def multiplication_fun(mult_nums):
    mult_result = mult_nums[0]
    for mult in mult_nums[1:]:
        mult_result *= mult
    return mult_result

def multiplication():
    print()
    mult_nums = []
    while True:
        mult_input = input("Enter a number to multiply or 'done' when finished: ")
        if mult_input == 'done':
            break
        try:
            mult = float(mult_input)
            mult_nums.append(mult)
        except ValueError:
            print("Error: Please enter a valid number or 'done' to finish")

    if len(mult_nums) < 2:
        print("Error: You need at least two numbers for multiplication")
    else:
        try:
            mult_result = multiplication_fun(mult_nums)
            print(f"After multiplying\n {mult_nums}\n your answer is {mult_result}")
        except Exception as e:
            print(f"Error: An error occurred during multiplication - {e}")

def division_fun(div_nums):
    div_result = div_nums[0]
    for div in div_nums[1:]:
        try:
            div_result /= div
        except ZeroDivisionError:
            print("Error: Division by zero occurred")
            return
    return div_result

def division():
    div_nums = []
    while True:
        div_input = input("Enter a number to divide or 'done' when finished: ")
        if div_input == 'done':
            break
        try:
            div = float(div_input)
            div_nums.append(div)
        except ValueError:
            print("Error: Please enter a valid number or 'done' to finish")

    if len(div_nums) < 2:
        print("Error: You need at least two numbers for division")
    else:
        try:
            div_result = division_fun(div_nums)
            if div_result is not None:
                print(f"After dividing\n {div_nums}\n your answer is {div_result}")
        except Exception as e:
            print(f"Error: An error occurred during division - {e}")

def calculator():
    print()
    while True:
        use = input("Would you like to use the calculator? (y/n): ").lower()
        if use == 'y':
            print("What would you like to do?")
            options = input("Options are: addition, subtraction, multiplication, or division.\n Type your answer: ").lower()
            if options == 'addition':
                addition()
            elif options == 'subtraction':
                subtract()
            elif options == 'multiplication':
                multiplication()
            elif options == 'division':
                division()
            else:
                print("Sorry, that's not an option at this time")
        elif use == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

# print()
# calculator()

# 3. The Event Planner

'''
Objective: The aim of this assignment is to simulate an event planning scenario where dates and times are crucial, and the handling of invalid date formats is necessary.

Task 1: Start
Create a function that accepts a date string from the user and attempts to convert it into a Python datetime object.
Use a try block to handle the conversion and catch ValueError if the user enters an invalid date format.

Task 2: Reminder Setup
If the date conversion is successful, allow the user to set a reminder for the event.
Use an else block to confirm the reminder setup and display the event date and time back to the user.

Task 3: User Guidance
In the except block, provide a clear explanation of the expected date format and prompt the user to try entering the date again.
Ensure that the user is thanked for using the event planner in a finally block, maintaining a positive user experience.
'''

from datetime import datetime

def convert_to_datetime(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj
    except ValueError:
        print("Error: Invalid date format. Please enter the date in YYYY-MM-DD format and try again.")

def set_reminder():
    try:
        date_string = input("Enter a date in YYYY-MM-DD format for your event: ")
        event_date = convert_to_datetime(date_string)
        if event_date:
            event_name = input("Enter the name of the event: ")
            print("Reminder set up successfully!")
            print(f"Your event '{event_name}' is scheduled on {event_date.strftime('%A, %B %d, %Y')}.")
            print(f"Don't forget it!")
    finally:
        print("Thank you for using the event planner!")

# set_reminder()

# 4. The Recipe Ratio Adjuster

'''
Objective: The aim of this assignment is to create a program that adjusts the quantities of a recipe based on the number of servings, handling any type of arithmetic errors or user input exceptions.

Task 1: Start
Ask the user for the number of servings the recipe is originally for and the number of servings they wish to make.

Ensure that the user inputs are valid numbers and handle any ValueError that arises from improper input.

Task 2: Quantity Calculation
Calculate the adjustment factor by dividing the desired servings by the original servings.

Use a try block to catch any arithmetic errors that may occur during the calculation.

Task 3: Serving Success
If the calculation is successful, display the adjusted recipe quantities to the user.

Use a finally block to print a message encouraging the user to enjoy their cooking, regardless of the outcome of the calculation.
'''

def adjust_recipe():
    try:
        original_servings = float(input("Enter the number of servings the recipe is originally for: "))
        desired_servings = float(input("Enter the number of servings you wish to make: "))
        
        adjustment_factor = desired_servings / original_servings
        
        print("\nAdjusted Recipe Quantities:")
        print(f"Original servings: {original_servings}")
        print(f"Desired servings: {desired_servings}")
        print(f"Adjustment factor: {adjustment_factor}")
    except ValueError:
        print("Error: Please enter valid numbers for the servings.")
    except ZeroDivisionError:
        print("Error: Number of original servings cannot be zero.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nEnjoy your cooking!")

# adjust_recipe()

# 5. The Time Zone Traveler

'''
Objective: The aim of this assignment is to create a program that converts the current time to the time in a user-specified time zone, handling any exceptions related to invalid time zone entries.

Task 1: Start
Prompt the user to enter their current time and the time zone they want to convert it to.

Use a try block to attempt the time zone conversion, catching any ValueError associated with an invalid time zone entry.

Task 2: Time Conversion
If the time zone is valid, calculate and display the current time in the specified time zone.

Use an else block to confirm the successful conversion to the user.

Task 3: Traveler's Aid
In the except block, provide a list of valid time zone options and ask the user to select from the list.

Include a finally block that wishes the user safe travels, ensuring a friendly end to the interaction regardless of the outcome.
'''

from datetime import datetime, timedelta

def convert_time():
    try:
        current_time_str = input("Enter your current time (format: HH:MM AM/PM): ")
        timezone_offset = float(input("Enter the desired time zone offset in hours (+/-). \nE.G (+1 hours to go up an hour or -1 to go down an hour): "))

        current_time = datetime.strptime(current_time_str, "%I:%M %p")

        converted_time = current_time + timedelta(hours=timezone_offset)
        
        print("\nConverted Time:")
        print(f"Current Time (GMT{timezone_offset:+}): {converted_time.strftime('%I:%M %p')}")

    except ValueError as e:
        print(f"Error: {e}")
        print("\nSafe travels!")


# convert_time()
        

def run_assignment():
    print()
    print("Welcome to my assignment!")
    grader = input("Please enter your name to continue: ")
    print(f"Thanks {grader}!")
    while True:
        print("-" * 50)
        print("Program Library:")
        print("1: Exceptional Weather Forecast")
        print("2: Calculator Concierge")
        print("3: The Event Planner")
        print("4: The Recipe Ratio Adjuster")
        print("5: The Time Zone Traveler")
        print("X: Exit")

        choice = input("Choose a program to run: ")
        if choice == '1':
            find_temp()
        if choice == '2': 
            calculator()
        if choice == '3': 
            set_reminder()
        if choice == '4':
            adjust_recipe()
        if choice == '5':
            convert_time()
        if choice == 'x':
            print(f"Thanks for taking the time to run through my assignment {grader}!")
            print("Have a great day!")
            break
        else:
            print("That's not a correct input, please try again")

run_assignment()