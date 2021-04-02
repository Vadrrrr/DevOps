user = input('There are 3 signs in front of you. Which one would you like to read?')
test1 = 'right'
if(user == 'right'):
    print('The right sign says: "DEAD PEOPLE ONLY"')
elif(user == 'left'):
    print('The left sign says: "BEWARE!"')
elif(user == 'middle'):
    print('The middle sign says: "CERTAIN DEATH"')
else :
    print(f'There is no {user} sign')