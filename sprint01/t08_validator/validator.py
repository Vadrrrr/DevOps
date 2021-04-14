import re

def validator(argument):
	res = argument.split(' ')
	op = res[1]
	if op == '':
		return False
	try:
		a = float(res[0])
		b = float(res[2])
		return check_op(op, a, b)
	except Exception as e:
		return False

        
def check_op(op, a, b):
	if op == '<':
		if a < b:
			return True
		else:
			return f'{a} > {b}'
	if op == '>':
		if a > b:
			return True
		else:
			return f'{a} < {b}'
	elif op == '<=':
		if a == b:
			return f'{a} == {b}'
		elif a <= b:
			return True
		else:
			return f'{a} >= {b}'
	elif op == '>=':
		if a >= b:
			return True
		elif a == b:
			return f'{a} == {b}'
		else:
			return f'{a} <= {b}'
	elif op == '==':
		if a == b:
			return True
		elif a <= b:
			return f'{a} <= {b}'
		elif a >= b:
			return f'{a} >= {b}'
	else:
		return False
