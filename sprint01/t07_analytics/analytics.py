def print_str_analytics(str):
    count = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0 
    for i in str:
        if(i.isalnum()):
            count = count + 1
        if(i.isalpha()):
            count1 = count1 + 1
        if(i.isdecimal()):
            count2 = count2 + 1
        if(i.islower()):
            count3 = count3 + 1
        if(i.isupper()):
            count4 = count4 + 1
        if(i.isspace()):
            count5 = count5 + 1
    print(f"""|------------------------------------------------|
|                String analytics                |
|------------------------------------------------|
| '{str}'
|------------------------------------------------|
| Number of printable characters is: {len(str)}
| Number of alphanumeric characters is: {count}
| Number of alphabetic characters is: {count1}
| Number of decimal characters is: {count2}
| Number of lowercase letters is: {count3}
| Number of uppercase letters is: {count4}
| Number of whitespace characters is: {count5}
|------------------------------------------------|""")

