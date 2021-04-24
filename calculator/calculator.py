import operator
action = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
    "**": pow
}

print(action['*'](100, 25)) # 2500
print(action['-'](100, 25)) # 75
print(action['**'](2, 8)) # 256


