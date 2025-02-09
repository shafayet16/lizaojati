'''# wowie we made it to day 2(data types,numbers,type conversions,operations,f-strings)
#integers-----------------
#we can select a character of a string by using [] and putting in the index of the char we want as arg, this is also called subscripting
print("hello"[4])

#anything inside a string is a string even numbers so the code below will just concatenate the two strings
print("123" + "345")

#numbers outside a string is deemed as interger,below is a normal sum print 
print(3999+670)

#when writing large numbers we use commas such as 345,679,978 but in python we can just use underscored instead of commas
print(123_456_789)

#floooooats in py(anything with a decimal)
print(3.14)

#the key to conditionals the damn booleans
print(True)

#checking previous day1 error
error = 7
solved_error = str(error)
print(solved_error + ' ' + "Days")

#type conversion exercise
user_input = input("what's your input?\n")
digit_one = int(user_input[0])
digit_two = int(user_input[1])
user_input_added = digit_one + digit_two
output = str(user_input_added)
print("Your two digits added: " + output)

#Mathematics in python
print(1+1)
print(1-1)
print(1*2)
print(9/3) #when doing division the result will be float
print(5**5)

#BMI calculator 
weight = int(input("What's your weight in kgs?\n"))
height = float(input("What's your height in meters?\n"))
Bmi = weight / height ** 2
Bmi_output = int(Bmi)
print(Bmi_output)

#rounding in python 
print(round(8/3)) #3
print(round(8/3,2)) #rounds up to two decimals = 2.67
print(8//3) #no bs direct 2 = how many times you can divide it by 3

 #assignment shorcuts
x = 5
x += 1 #x = x + 1
x -= 1 #x = x - 1
x *= 2 #x = x * 2 
x /= 2 #x = x / 2
x %= 2 #x = x % 2

#f-string
name = "John"
age = 30
print(f"Hello, my name is {name} and I'm {age} years old.")

#your life in weeks

year = 52
average_life = 90
user_age = int(input("What's your age?\n"))
weeks_left = (average_life - user_age) * year
print(f"The weeks you have left in your life: {weeks_left}")

#Tip calculator
print("Greetings this is my tip calculator")
total_bill = float(input("What's the total bill?\n"))
tip_percentage = float(input("What percentage of tip would you like to give?\n"))
split = int(input("How many people will split the bill?\n"))
tip = round((total_bill * tip_percentage / 100 + total_bill) / split,2)
print(f"Each person should pay: {tip}")
#congo broksi you actually cooked it,make these two a big project using html,css and js or python and put it in your portfolio.'''
#tip calculator rehearse
greetings = print("Greetings this is my tip calculator")
total_bill = float(input("What's the total bill?\n"))
people = int(input("How many people will split the bill?\n"))
tip = float(input("What percentage of tip would you like to give?\n"))
tip_percentage = tip / 100
total_tip = total_bill * tip_percentage
total_bill += total_tip
bill_per_person = total_bill / people
final_amount = round(bill_per_person,2)
print(f"Each person should pay: {final_amount}")