import pandas as pd

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pd.read_csv('nato_phonetic_alphabet.csv')

alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ")
nato_list = [alphabet_dict[item] for item in word.upper() if item in alphabet_dict.keys()]
print(nato_list)
