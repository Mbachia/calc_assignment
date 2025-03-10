def my_calc(number1,number2, sign):
    if sign == "+":
        return number1 + number2
    elif sign == "-":
        return number1 - number2
    elif sign == "*":
        return number1 * number2
    elif sign == "/":
        if number2 == 0:
            print("number cant be divided by zero")
        return number1/number2
    

number_1 = float(input("please enter first number:"))
number_2 = float(input("please enter second number:"))
sign = input('please enter arithmetic sign:')
results = my_calc(number_1,number_2,sign)
print(results)