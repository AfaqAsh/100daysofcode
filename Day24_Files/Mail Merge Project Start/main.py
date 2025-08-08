#TODO: Create a letter using starting_letter.txt 
with open("./Input/Letters/starting_letter.txt") as data:
    letter = data.readlines()

#for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as data:
    content = data.read().split()
    
#Replace the [name] placeholder with the actual name.
for name in content:
    letter_name = f'letter_for_{name}'
    first_line = f'Dear {name}\n'
    letter[0] = first_line #
    new_letter = ''.join(letter)
    with open(f"./Output/ReadyToSend/{letter_name}", mode='w') as data:
        data.write(new_letter)
    print(letter)
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
