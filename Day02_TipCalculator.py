# Coding Challenge
# givenNumber = input("Enter a number: ")
# total = 0
# for i in givenNumber:
#     total = total + int(i)

# print(total)    

print("Welcome to the Tip Calculator")
totalBill = input("What was the total bill? ")

try:
    totalBill = float(totalBill)
except:
    print("Enter the total amount as digits only")

tipPercentage = int(input("What percentage of tip would you like to give? "))
numOfPeople = int(input("How many people to split the bill? "))

individualAmount = round((totalBill * (tipPercentage/100 + 1)) / numOfPeople, 2)
print(f"Each person should pay ${individualAmount}")

# In the Day02, the new thing I learnt was the f-strings. It is quite similar to the backtick strings in Javscript and
# helps in referencing and printing variables directly in a string statement


