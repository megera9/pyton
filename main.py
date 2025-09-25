a = float(input('введите 1е число'))
b = float(input('введите 2е число'))

while True:
    action = input("введите действие + - / * // ** % == != > < >= <=")
    result = 0
    if action == "+":
        result = a + b
    elif action == "-":
        result = a - b
    elif action == "*":
        result = a * b
    elif action == "**":
        result = a ** b
    elif action == "/":
        if a  == 0 or b == 0:
            result = "ошибка"
        else: 
            result = a / b

    elif action == "//":
        if a  == 0 or b == 0:
            result = "ошибка"
        else: 
            result = a // b
    elif action == "%":
        if a  == 0 or b == 0:
            result = "ошибка"
        else: 
            result = a % b
    elif action == "==":
         result = a == b
    elif action == "!=":
        result = a != b
    elif action == ">":
        result = a > b
    elif action == "<":
        result = a < b
    elif action == ">=":
        result = a >= b
    elif action == "<=":
        result = a <= b
    else:       
        continue
    print(result)
    break
