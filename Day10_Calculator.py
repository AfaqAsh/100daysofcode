import math

def calculator(fnum, snum, operator):
    """The functions takes two number and a operator to perform a calculation to return a number"""
    if operator == '+':
        return fnum + snum
    elif operator == '-':
        return fnum - snum
    elif operator == '*':
        return fnum * snum
    elif operator == '/':
        return fnum / snum
    else:
        return "Input valid operator"

quit = False
choice = 'n'
while not quit:
    if choice == 'n':
        first_num = int(input('What is the first number: '))
        operator = input("Pick an operation from the following:\n+\n-\n*\n/\nEnter your choice: ")
        second_num = int(input('What is the second number: '))
        result = calculator(first_num, second_num, operator)
        print(f'{first_num} {operator} {second_num} is {result}')
        
    else:
        operator = input("Pick an operation from the following:\n+\n-\n*\n/\nEnter your choice: ")
        second_num = int(input('What is the second number: '))
        result_temp = result
        result = calculator(result, second_num, operator)
        print(f'{result_temp} {operator} {second_num} is {result}')
    
    choice = input(f"Press y to continue calculation with the last number {result} or press n to start a new calculation or x to exit the program")
    if choice == "x":
        quit == True

# Learnt about docstrings """ Description goes in the triple quotation marks here """