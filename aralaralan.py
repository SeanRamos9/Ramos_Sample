num1= int(input("Give me a number: "))
num2= int(input("Second number: "))
operation=(input("What kind of operation: "))
Add= num1 + num2
Sub= num1 - num2
Multi= num1 * num2
Divi= num1 / num2
if (operation=="Addition"):
    print(Add)
elif (operation== "Minus"):
    print(Sub)
elif (operation== "Multiply"):
    print(Multi)
elif (operation== "Divide"):
    print(Divi)
else:
    print("error")