while True:
    num1=int(input("Enter The 1st Number :- "))
    opr = input("Enter The Operator :- ")
    num2=int(input("Enter 2nd Number :- "))
    if opr == "+":
        sum = num1+num2
        print("The Answer is:-",sum)
    elif opr == "-":
        sub = num1-num2
        print("The Answer is:-",sub)
    elif opr == "*":
        mul = num1*num2
        print("The Answer is:-",mul)
    elif opr == "/":
        div = num1/num2
        print("The Answer is:-",div)
    else:
        print("Invalid Operator")
