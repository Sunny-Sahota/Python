from math import sqrt

#Drawing a Shape 
def draw_shape():
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
#Within python spaces in words fill with '_'
'''
Use this for comments
'''
def data_types(): 
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

    name = input("Enter you name: ")
    age = input("Enter age: ")
    print("hello "+ name + "!" + "you are " + age + " yrs old.")

#Lists, indexed from 0
def lists():
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

##Tuples , imutable = cant be changed or modified 
def Tuples():
    coordinates_one = (4 , 5)
    coordinates = [(4, 5), (6 , 7), (134 , 56)]

    print(coordinates[1])

#Functions
def say_hi(name, age):
    print("Hello " + name + " you are "+ age)

#say_hi("Mike", "67")

def cube(num):
    return num*num*num

#result = cube(4)
#print(result)

#Dictionaires
def dictionary():     
    monthConversions = {
        "Jan" : "January",
        "Feb" : "February",
        "Mar" : "March",
        "Apr" : "April",
        "May" : "May",
        "Jun" : "June",
        "Jul" : "July",
        "Aug" : "August",
        "Sep" : "Sepetember",
        "Oct" : "October",
        "Nov" : "November",
        "Dec" : "December"
    }

#While loops 
def While_loops():
    i = 1
    while i <= 10:
        print(i)
        i += 1

    print("Done with loop")

    #Could use this for password 
    secret_word = "yes"
    guess = ""

    while guess != secret_word:
        guess = input("Enter guess: ")

    print("You win!")   

#For loops 
def For_loops():
    for letter in "I am Coding something":
        print(letter)

#Exponent 
def exponents():
    print(2**3)

    def raise_to_power(base_num, pow_num):
        result = 1
        for index in range(pow_num):
            result = result * base_num
        return result 

    print(raise_to_power(2,3))

#2D Lists & Nested Loops
def TwoD_Lists_Nested_Loops():
    number_grid = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [0]
    ]

    print(number_grid[0][0])

    for row in number_grid:
        for col in row:
            print(col)

def count_vowels(phrase):
    count = 0
    for letter in phrase: 
        if letter.lower() in "aeiou":
            count = count + 1 
    return count

#print(count_vowels(input("Enter a phrase: ")))