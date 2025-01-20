#damn bro is grinding through the night frfr, so proud of bro(python loops - for loops,ranges and code blocks)
#a simple for loop(takes a var called fruit and uses it to iterate all of the items in the list)
"""fruits = ['peach','cherry','apple']
for fruit in fruits:
    print('Big ' + fruit + ' pie')
#height average exercise
student_heights = input("Enter student heights separated by spaces: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# Calculate the average
total_height = 0
length = 0
for height in student_heights:
    total_height += height
    length += 1
average_height = total_height / length
print(average_height)
#highest score
highest_height = student_heights[0]
for score in student_heights:
    if score > highest_height:
        highest_height = score
print("The highest height is:", highest_height)
#range loop
sum = 0
for i in range(1,101):
    sum += i
print(sum)
#even number sumation program
n = int(input("What's the range?\n"))
sum = 0
for i in range(2, n+1, 2):
    sum += i
print("This is your even number summation", sum)"""
#random letter generator
import random

password = ''
'''rand_length = int(input("length?\n"))'''
rand_num_length = int(input("How many numbers?\n"))
rand_letter_length = int(input("How many letters?\n"))
rand_symbol_length = int(input("How many symbol?\n"))
letter ='abcdefghijklmnopqrstuvwxyz'
symbol = '!@#$%^&*'
num = '123456789'
password_list = []
riyal_password = ''
"""
for i in range(0,rand_length):
    rand_index = random.randint(0,len(letter))
    rand_letter = letter[rand_index - 1]
    rand_num_index = random.randint(0,len(num))
    rand_num = num[rand_num_index - 1]
    rand_symbol_index = random.randint(0,len(symbol))
    rand_symbol = symbol[rand_symbol_index - 1]
    rand = [rand_letter,rand_num,rand_symbol]
    password += random.choice(rand)"""
for i in range(1,rand_num_length + 1):
    rand_nums = random.choice(num)
    password += rand_nums
for i in range(1,rand_letter_length + 1):
    rand_letters = random.choice(letter)
    password += rand_letters
for i in range(1,rand_symbol_length + 1):
    rand_symbols = random.choice(symbol)
    password += rand_symbols
print(password)