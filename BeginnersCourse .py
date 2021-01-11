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

