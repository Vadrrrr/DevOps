n = int(input('n: '))
a = int(input('a: '))
b = int(input('b: '))

result = (lambda x :True if x == n else False)(a * b)

print(result)