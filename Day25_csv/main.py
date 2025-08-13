import csv
import pandas as pd

# with open("002 weather-data.csv") as data:
#     content = data.readlines()
    
# print(content)

# with open('002 weather-data.csv') as data:
#     content = csv.reader(data)
#     temperatures = []
#     next(content)
#     for row in content:
#         temperatures.append(int(row[1]))
#     print(temperatures)

# content = pd.read_csv('002 weather-data.csv')
# print(content['temp'])
# print(type(content))
# data_dict = content.to_dict()
# print(data_dict['day'])

# def average_temp(data):
#     total = 0
#     for entry in data:
#         total += entry
#     return total/len(data)

# temp = content['temp']
# mean_temp = temp.mean()
# max_temp = temp.max()
# print(max_temp)

# mond = content[content['temp'] == content['temp'].max()]
# print(mond)

# data_dict = {
#     'students': ['Alicia', 'Maelle', 'Verso'],
#     'ages': [17,17,26]
# }

# data = pd.DataFrame(data_dict)
# data.to_csv('new_csv.csv')
# print(data)

squirrels = pd.read_csv("Central-Park-Squirrel-Census-Squirrel-Data.csv")
new_squirrels = squirrels['Primary Fur Color'].value_counts()
dict_data = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count' : []
}

for color in new_squirrels:
    dict_data['Count'].append(color)

# print(type(new_squirrels))
colors = pd.DataFrame(dict_data)
# colors.columns = ['Fur Color', 'Count']
print((colors))