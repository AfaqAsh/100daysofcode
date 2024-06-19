import random
import string

# *Exercise 1 - Average Height Finder
# student_heights = input("Enter student heights separated by commas: ").split(',')
# total = 0
# for i in range(0, len(student_heights)):
#     total = total + int(student_heights[i])

# average_height = total / len(student_heights)
# print(f'The average height of the students is {average_height}')

# *Exercise 2 - Highest Score Generator
# student_scores = input("Enter student scores separated by commas: ").split(',')
# highest_score = int(student_scores[0])
# for i in range(1, len(student_scores)):
#     if int(student_scores[i]) > highest_score:
#         highest_score = int(student_scores[i])

# print(f'The highest score of the students is {highest_score}')

# *Exercise 03 - Adding Even Numbers
# total = 0
# for number in range(1,101):
#     if (number % 2 == 0):
#         total += number

# print(total)

# *Exercise 04 - FizzBuzz
# for number in range(1,101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print('Buzz')
#     else:
#         print(number)

# *Main Exercise - Password Generator
letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

num_letters = int(input('Input number of letters: '))
num_numbers = int(input("Input number of digits: "))
num_symbols = int(input("input number of symbols: "))

total_length = num_letters + num_numbers + num_symbols
generated_password = []

for i in range(0, num_letters):
    generated_password.append(letters[random.randint(0, len(letters) - 1)])

for j in range(0 , num_numbers):
    generated_password.append(numbers[random.randint(0, len(numbers) - 1)])

for k in range(0 , num_symbols):
    generated_password.append(symbols[random.randint(0, len(symbols) - 1)])

random.shuffle(generated_password)
final_password = ''.join(generated_password)
print(f'The generated password is: {final_password}')

# * Did not learn anything new but revised some concepts