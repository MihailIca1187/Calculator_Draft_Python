num1 = int(input("First number:"))
print (num1)
num2 = int(input("Second number:"))
print (num2)
operation = input( '''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
if operation == '+' :
    print('{} + {} = '.format(num1, num2))
    print(num1 + num2)
elif operation == '-' :
    print('{} - {} = '.format(num1, num2))
    print(num1 - num2)   
elif operation == '*' :
    print('{} * {} = '.format(num1, num2))
    print(num1 * num2)
elif operation == '/' :
    print('{} / {} = '.format(num1, num2))
    print(num1 / num2)    
else:
    print('I do not know what you speak of.')
