"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
status = True
while status == True:
    input_string = input()
    token = input_string.split(' ')

    for item in token:
        if item == 'q':
            exit()
    num1 = float(token[1])
    try:
        num2 = float(token[2])
    except:
        num2 = 0
    if token[0] == '+':
        result = add(num1,num2)
        print(result)
    elif token[0] == '-':
        result = subtract(num1, num2)
        print(result)
    elif token[0] == '*':
        result = multiply(num1, num2)
        print(result)
    elif token[0] == '/':
        result = divide(num1, num2)
        print(result)
    elif token[0] == 'square':
        result = square(num1)
        print(result)
    elif token[0] == 'cube':
        result = cube(num1)
        print(result)
    elif token[0] == 'pow':
        result = power(num1, num2)
        print(result)
    elif token[0] == 'mod':
        result = mod(num1, num2)
        print(result)