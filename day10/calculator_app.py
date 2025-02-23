def addition(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return 'Cannot divide by zero'
    return num1 / num2

operations_dict = {
    '+': addition,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator(num1, num2, operation):
    if operation in operations_dict:
        operation = operations_dict[operation]
        try:
            result = operation(num1, num2)
            return result
        except ZeroDivisionError:
            return 'Cannot divide by zero'
    else:
        return 'Invalid operation'

if __name__ == '__main__':
    print("Welcome to the calculator app")
    try:
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        operation = input('Enter operation (+, -, *, /): ')
        print(f'{calculator(num1, num2, operation)}')
    except ValueError:
        print('Invalid input. Please enter numeric values.')