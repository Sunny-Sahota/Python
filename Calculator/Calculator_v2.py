#Use dictionary to compare string value to actual
operators = {
    '+': "add",
    '-': "sub",
    '*': "mul",
    '/': "div",
    '%': "mod"
}

def calculate(user_input):
    
    for c in operators.keys():
        #seperate the logic within the string
        left, operator , right = user_input.partition(c)

        if operator in operators:
            if(operator == "+"):
                result = int(left) + int(right)
            elif(operator == "-"):
                result = int(left) - int(right)
            elif(operator == "*"):
                result = int(left) * int(right)
            elif(operator == "/"):
                result = float(left) / float(right)
            elif(operator == "%"):
                result = float(left) % float(right)
            return result

print("  ___________________________________")
print(" / Welcome To Sunny's Calculator v2 /")
print("/__________________________________/")

user_choice = [("True"),("Yes"),("Y"),("Sure")]

run_app = True

while(run_app):
    selected = input("\nWould you like to use the calculator: ")

    for choice in user_choice:
        if selected == choice:
            calc = input("Type calculation : \n")
            print("\nAnswer : " + str(calculate(calc)))
            run_app = True
            break
        else:
            run_app = False
