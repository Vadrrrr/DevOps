first = str(input('Enter your first string: '))
second = str(input('Enter your second string: '))
if not first or not second:
    print('One of the strings is empty.')
else:
    command = input('Enter your command: ')
    if(command == 'concat'):
        conca = first + ' ' + second
        print(f'Your string is: {conca}')
    elif(command == 'find'):
        for i in range(len(second)):
            if second[i] == first[i]:
                if i == len(second) - 1:
                    print('True')
                    break
        else:
            print ('False')
    elif(command == 'beatbox'):
        a = int(input('Enter your first beatbox number: '))
        b = int(input('Enter your second beatbox number: '))
        c = int(1)
        for c in range(a):
            print(f'{first}',end='')
        for c in range(b):
            print(f'{second}',end='')
            if (c == b - 1):
                print(f'{second}',end='\n')
                break
    else :
        print('usage: command find | concat | beatbox')