
def add(a,b):
    return a+b


def mul(a,b):
    return a*b


def div(a,b):
    if b == 0:
        raise ValueError('Cannot divide with Zero')
    else:
        return a / b
