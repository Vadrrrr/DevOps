

def calculator(op,di1,di2):
    global operation

    operation = {"add": lambda: di1 + di2,
                 "sub": lambda: di1 - di2,
                 "mul": lambda: di1 * di2,
                 "div": lambda: di1 / di2,
                 "pow": lambda: di1 ** di2}
    if op not in operation:
        raise ValueError ("Invalid operation. Available operations: add, sub, mul, div, pow.")
    if not isinstance(di1, (int , float)) or not isinstance(di2, (int , float)):
        raise ValueError ("Invalid numbers. Second and third arguments must be numerical.")
    else:
        return operation[op]()
