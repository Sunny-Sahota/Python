import random
import string #ascii_library 

def get_password(length):
    letter = string.ascii_lowercase
    result_str = ''.join(random.choice(letter) for i in range(length))
    print("Random string of length", length, "is:", result_str)


#get_password(10)

def get_password2(length):

    if user_selec1 == "n" or user_selec2 == "n":
        choice = string.digits
        num_str = ''.join(random.choice(choice) for i in range(length))
    if user_selec1 == "l" or user_selec2 == "l":
        choice = string.ascii_letters
        letter_str = ''.join(random.choice(choice) for i in range(length))
    if user_selec1 == "sc" or user_selec2 == "sc":
        choice = string.punctuation
        sc_str = ''.join(random.choice(choice) for i in range(length))

    print(num_str + letter_str)

    #a method to sort what ascii to use
    # return the set of random string of that type
    # put it all together then randomise that
#print("Type what you would like your password to be made from;")
#user_selec1, user_selec2 = input("Number = n, Letters = l, Special Characters = sc : ").split()




def get_password3():
    letters = string.ascii_letters
    num = string.digits
    symbol = string.punctuation

    array = list()
    n = int(input("enter how many types you want to include in the password :"))

    for i in range(0,n):
        
        array.append(string(input()))
    
    print(array)
        
get_password3()
    