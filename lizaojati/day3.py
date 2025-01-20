#wowieee broski got into day 3 dayum and you didn't stop crazy grind frfr(conditional statements,logical operators,code blocks, scope)
#conditional statements in python
day = 'friday'
if day == 'friday':
    print("weekend")
else:
    print('work')
    
#logical operators in python = ( >,<,>=,<=,=,==,!= ) ik what this means os need to be descriptive

#is the number odd or even program
user_input = int(input("What's your selected number to check?\n"))
if user_input % 2 == 0:
    print(f"{user_input} is an even number.")
else:
    print(f"{user_input} is an odd number.")

#nested if/else statement using an amusement part roller coaster ticket entry
print("Welcome to the rollercoaster, please elaborate with the questions to buy tickets")
height = int(input("What's your height in cm?\n"))
ticket = 0
if height<120:
    print("You're not tall enough for the roller coaster")
elif height >= 120:
    age = int(input("What's your age?\n"))
    photos = input("do you want photos?")
    if age <= 12:
        ticket = 7
    elif age <= 18:
        ticket = 10
    elif age >=45 or age <=55:
        print("Everything's free don't worry")
    else:
        ticket = 14
    if photos == 'yes':
        ticket += 3
        print(f"Your total price is {ticket}$")
    else:
        print(f"Your total price is {ticket}$")

    
#bmi 2.0
print("Welcome to the upgraded bmi calculator")
weight = float(input("What's your weight in kg?\n"))
height = float(input("What's your height in meters?\n"))
bmi = weight / (height ** 2)
if bmi <= 18.5:
    print(f"{bmi}, Underweight")
elif bmi <= 25:
    print(f"{bmi}, Normal weight")
elif bmi <= 30:
    print(f"{bmi}, Lil bulky")
else:
    print(f"{bmi}, Obese, Stop eating start gyming")
    
#stupid ahh leap year program
year = int(input("What's the year?\n"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
    
#pizzarea bill program
print("Welcome to the pizzarea")
bill = 0 
size = input("What size of pizza do you want? S,M,L\n")
peperroni = input("Do you want peperroni?Y,N\n")
cheese = input("Do you want extra cheese?Y,N\n")
if size == 'S':
    bill+=15
    if peperroni == 'Y':
        bill+=2
    if cheese == 'Y':
        bill+=1
    print(f"Your bill is {bill}$")
elif size == 'M':
    bill+=20
    if peperroni == 'Y':
        bill+=3
    if cheese == 'Y':
        bill+=1
    print(f"Your bill is {bill}$")
elif size == 'L':
    bill+=25
    if peperroni == 'Y':
        bill+=3
    if cheese == 'Y':
        bill+=1
    print(f"Your bill is {bill}$")     
    
#love calculator
your_name = input("what's your name?\n")
their_name = input("what's their name?\n")
combined_name = (your_name + their_name).lower()
t = combined_name.count('t')
r = combined_name.count('r')
u = combined_name.count('u')
e = combined_name.count('e')
match1 = t + r + u + e
l = combined_name.count('l')
o = combined_name.count('o')
v = combined_name.count('v')
e = combined_name.count('e')
match2 = l + o + v + e
total_lovescore = str(match1) + str(match2)
lovescore = int(total_lovescore)
if lovescore <= 10 and lovescore >= 90:
    print(f"lovescore: {lovescore} Fuchka aar tok")
elif lovescore >= 30 and lovescore >= 60:
    print(f"lovescore: {lovescore} it's aight ig")
else:
    print(f"lovescore: {lovescore} Good luck....")
#Role Playing game program day 3 final project
print("Welcome to the role playing game made my simsim(me)")
print("Your job is to find the tresure")
Beginning = input("You are in a village, there is no one,it is abandoned. select 'check houses' or 'go to the lake'\n")
if Beginning == 'check houses':
    house = input("You find a rusty magnum revolver,'go to the trees' or 'go to the mansion'\n")
    if house == 'go to the mansion':
        mansion = input("there are 2 doors,'left' or 'right'\n")
        if mansion == 'left':
            room = input("There's an old woman, 'go close to her' or 'shoot'\n")
            if room == 'go close to her':
                print("she dissapears, and you see the tresure")
        else:
            print("She is a vampire she tears you apart, Game over")   
    else:
        print("There's someone behind you, Game over")
else:
    print("There is a large python at the lake, Game over")
#wowie bro finished the game with his wifey ain't no way