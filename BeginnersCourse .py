from math import *

#Drawing a Shape 

shape = "pep"

if(shape == "tri"):
    print("   /|")
    print("  / |")
    print(" /  |")
    print("/___|")
elif(shape == "sqr"):
    print("________")
    print("|      |")
    print("|      |")
    print("|______|")
elif(shape == "rec"):
    print("_____")
    print("|   |")
    print("|   |")
    print("|___|")
else:
    print("Sorry you didn't select a correct shape name!! Please try again!!")

#Variables / data types
#within python spaces in words fill with '_'

player_name = "SillyBillyBoy"
player_age = 2
is_male = False

#Make sure to parse your other types(int's , bool's backs into strings)
print ("My name is " + player_name +" ,I am "+ str(player_age) + "yrs old"+  "\n. Is this person ? : " + str(is_male))

#String manipulation
print("\n")
#  
phrase = "Wonderful Wimpy Wally World"
print(phrase.upper().isupper())
print(phrase.lower())

##To get the length of a string : 
print(len(phrase))
print(phrase[4])

#Retrive the index value at 'x'
print(phrase.index("f"))

print(phrase.replace("Wimpy","Wizz"))

#Numbers
#Remainders
print(30 % 9)

my_num = -4
print(abs(my_num)) # Absolute value
print(pow(3,2))
print(max(4,5,6,7)) # min, round

#must use math library for these functions 
x = sqrt(37)
print(round(x,3))

#getting an input from user , using a prompt

#name = input("Enter you name: ")
#age = input("Enter age: ")
#print("hello "+ name + "!" + "you are " + age + " yrs old.")

#Lists, indexed starting from 0
food = ["Apple", False, "Pizza", "Ice-cream", 156 ]

#To get the value at the back of the list 
print(food[-1])
#Get value from list, and everything after 
print(food[2:])

food[1] = True
#Get values in range, 1 to < 4
print(food[1:4])

##List Functions
lucky_numbers = [3,6,9,3,5]
animals = ["Dog", "Parrot", "Cat" , "Dog", "Fish"]

animals.extend(lucky_numbers)
animals.append("Batman")
animals.insert(2, "whale")
animals.remove("Cat")
#lucky_numbers.clear()

#Removes last element in list 
animals.pop() 

print(animals.index("Parrot"))
print(animals.count("Dog"))

lucky_numbers.sort() # Ascending
lucky_numbers.reverse()
print(lucky_numbers)

animals2 = animals.copy()

##Tuples
#imutable , cant be changed or modified 
#coordinates = (4 , 5)
coordinates = [(4, 5), (6 , 7), (134 , 56)]

print(coordinates[1])

#Functions

def say_hi(name, age):
    print("Hello " + name + " you are "+ age)

say_hi("Mike", "67")

def cube(num):
    return num*num*num

result = cube(4)
print(result)

is_male = True
is_tall = True

if is_male or is_tall:
    print("Is a male")
else:
    print("Is not male")