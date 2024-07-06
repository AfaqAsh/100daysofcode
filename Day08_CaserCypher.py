from math import ceil, sqrt
import string
# *Exercise 1 - Paint need to be bought

# def paint_calculator (height, width, cover):
#     return (ceil((height * width) / cover))

# test_h = int(input("Input the height of the wall: "))
# test_w = int(input("Input the width of the wall: "))
# test_calc = paint_calculator(height = test_h, width = test_w, cover = 5)
# print(test_calc)

#  *Exercise 2 - Prime number checker
# def check_prime(number):
#     isPrime = True
#     for i in range(2, ceil(sqrt(number)) + 1):
#         if (number % i == 0):
#             isPrime = False
#     return isPrime

# num = int(input("Enter a number you want to check is prime or not: "))
# print(check_prime(num))

#  *Caeser Cipher
characters = list(string.ascii_lowercase)
def caesar(message, shift, choice):
    new_message = []
    if (choice == "encrypt"):
        for n in range(0, len(message)):
            offset = ((characters.index(message[n]) + shift) % 26)
            new_message.append(characters[offset])
        
    elif (choice == "decrypt"):
        for n in range(0, len(message)):
            offset = ((characters.index(message[n]) - shift) % 26)
            new_message.append(characters[offset])
        
    print(''.join(new_message))
    
quit = False
while (not quit):
    choice = input("Type encode to encrypt and decode to decrypt: ")
    message = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    caesar(message, shift, choice)
        
    cont = input("Press c to continue or x to exit: ")
    if (cont == 'x'):
        quit = True
    

# Learnt about the difference between positional (1, 2, 3) and keyword arguments (a = 1, b= 2, c =3)