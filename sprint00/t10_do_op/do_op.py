print('---- Simple calculator ----')
print("Let's add some numbers")
first = input('Input your first value: ')
operator = input('Input your operator: ')
second = input('Input your second value: ')
first = int(first)
second = int(second)
if(operator == '+') :
    print(f'{first} {operator} {second} = {first + second}')
elif(operator == '-') :
    print(f'{first} {operator} {second} = {first - second}')
elif(operator == '*') :
    print(f'{first} {operator} {second} = {first * second}')
elif(operator == '/') :
    print(f'{first} {operator} {second} = {first / second}')
else :
    print("usage: the operator must be '*' or '+' or '-' or '/'")
print('---- Simple calculator ----')