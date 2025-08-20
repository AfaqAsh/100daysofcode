import random
import pandas as pd

number = [1, 2, 3]
number_inc = [n + 1 for n in number]
print(number_inc)

double_list = [n * 2 for n in range(1, 5)]
print(double_list)

names = ['Angela', 'John', 'Alex', 'Mary', 'Max', 'Chloe']
short_names = [name.upper() for name in names if len(name) > 5]
print(short_names)

# square
fib_seq = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
fin_sqr = [n * n for n in fib_seq]
print(fin_sqr)

# even
fib_even = [n for n in fib_seq if n % 2 == 0]
print(fib_even)

with open('num1.txt') as data:
    content = data.readlines()
    
with open('num2.txt') as data:
    content2 = data.readlines()
     
result = [int(n) for n in content if n in content2]
print(result)

scores = {name:random.randint(1, 100) for name in names}
print(scores)

passed_students = {student:score for (student, score) in scores.items() if score > 60}
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
word_count = {word:len(word) for word in sentence.split()}
print(word_count)

weather_c = {
    "Monday" : 12,
    "Tuesday" : 14,
    "Wednesday" : 15,
    "Thursday" : 14,
    "Friday" : 21,
    "Saturday" : 22,
    "Sunday" : 24
}

weather_f = {day:(temp * 9/5) + 32 for (day, temp) in weather_c.items()}
print(weather_f)

student_dict = {
    "students" : ["Angela", 'John', 'Alex', 'Mary' ],
    "scores" : [22, 33,66, 55]
}

student_data_frame = pd.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    print(row)