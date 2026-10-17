print("Calculator")
symb = ["+", "-", "*", "/", "%", "!=", "<", ">", "<=", ">=", "√", "x²","±", "x³", "xⁿ", "x!", "π"]
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
print("If you need help, type 'yes' to see the list of symbols.")
help = input("Do you need help? (yes/no): ")
if help.lower() == "yes":
    print(symb)
    print("Copy your choosen symbol and paste it in the next input.")
sym = input("Enter the symbol to calculate (in symbol): ")
if sym in symb:
    if sym == "+":
        result = num1 + num2
    elif sym == "-":
        result = num1 - num2
    elif sym == "*":
        result = num1 * num2
    elif sym == "/":
        result = num1 / num2
    elif sym == "%":
        result = num1 % num2
    elif sym == "!=":
        result = num1 != num2
    elif sym == "<":
        result = num1 < num2
    elif sym == ">":
        result = num1 > num2
    elif sym == "<=":
        result = num1 <= num2
    elif sym == ">=":
        result = num1 >= num2
    elif sym == "√":
        result = num1 ** 0.5
    elif sym == "x²":
        result = num1 ** 2
    elif sym == "±":
        result = -num1
    elif sym == "x³":
        result = num1 ** 3
    elif sym == "xⁿ":
        result = num1 ** num2
    elif sym == "x!":
        import math
        result = math.factorial(num1)
    elif sym == "π":
        import math
        result = math.pi
        result = float(num1)
    print(f"The result of {num1} {sym} {num2} is: {result}")
    print("Do you continue calculating with the answer? (yes/no): ")
    continue_calc = input().lower()
    if continue_calc == "yes":
        num1 = result
        num2 = int(input("Enter the next number: "))
        print(symb)
        sym = input("Enter the symbol to calculate (in symbol): ")
if sym in symb:
    if sym == "+":
        result = num1 + num2
    elif sym == "-":
        result = num1 - num2
    elif sym == "*":
        result = num1 * num2
    elif sym == "/":
        result = num1 / num2
    elif sym == "%":
        result = num1 % num2
    elif sym == "!=":
        result = num1 != num2
    elif sym == "<":
        result = num1 < num2
    elif sym == ">":
        result = num1 > num2
    elif sym == "<=":
        result = num1 <= num2
    elif sym == ">=":
        result = num1 >= num2
    elif sym == "√":
        result = num1 ** 0.5
    elif sym == "x²":
        result = num1 ** 2
    elif sym == "±":
        result = -num1
    elif sym == "x³":
        result = num1 ** 3
    elif sym == "xⁿ":
        result = num1 ** num2
    elif sym == "x!":
        import math
        result = math.factorial(num1)
    elif sym == "π":
        import math
        result = math.pi
    print(f"The result of {num1} {sym} {num2} is: {result}")
else:
    print("Invalid symbol entered.")