print("Calculator")
num=(int(input("Enter a Number : ")))
add=(int(input("Enter Another Number : ")))
sym=input("Enter the Symbol to calculate : ")
if sym == "+":
    print(num+add)
elif sym == "-":
    print(num-add)
elif sym == "*":
    print(num*add)
elif sym == "/":
    print(num/add)
else:
    print ("Enter a symbol from +, -, *, / ")