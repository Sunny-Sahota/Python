#Calculator
while(True):

    #Get and Store input of users 
    print("  ___________________________________")
    print(" / Welcome To Sunny's Calculator v1 /")
    print("/__________________________________/")

    user_operator =input("\nPlease enter the operator you would like, ( + , - , * , / ) : ")

    first_operand = input("Enter first number: ")
    second_operand = input("Enter second number: ")

    #Verifiy if the Equation was Correct
    user_choice = input("\nIs this equation correct, ( " + first_operand + " " + user_operator + " " + second_operand + " ), Y / N : ")

    #Verifying logic
    if(user_choice == "N"):
        print("\n----------Okay lets go again!!----------") 
    else:
        #Doing the actual Calulation
        if(user_operator == "+"):
            result = int(first_operand) + int(second_operand)
        elif(user_operator == "-"):
            result = int(first_operand) - int(second_operand)
        elif(user_operator == "*"):
            result = int(first_operand) * int(second_operand)
        elif(user_operator == "/"):
            result = float(first_operand) / float(second_operand)
        else:
            print("Error!! The operator you entered is incorrect...")
        #Print result
        print("Result = " + str(round(result, 3)))
    