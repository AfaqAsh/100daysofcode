# Each object has two things. What it has (attributes) and what it does (methods)
#  Class is the main blueprint while Objects are the instances that are generated from that Class
# Class  is named using the PascalCase while functions are created using the snake_case

from turtle import Turtle, Screen
from prettytable import PrettyTable

# tom = Turtle()
# my_screen = Screen()
# print(my_screen.canvheight)
# tom.shape('turtle')
# tom.color("#2A21AF")
# tom.forward(100)
# tom.left(120)
# tom.forward(200)
# tom.left(150)
# tom.forward(180)
# my_screen.exitonclick()

table = PrettyTable()
table.add_column('Pokemon', ['Charizad', 'Pikachu', 'Bulbasaur', 'Charmander', 'Mewto'])
table.add_column('Type', ['Fire', 'Electric', 'Grass', 'Fire', 'X'])
table.add_row(['Raichuu', 'Electric'])
table.border = True
table.align = 'l'
print(table)