import operator 
n1, opp, n2 = float(input("Enter the first number!\n")), input("Enter the operator you wish to use!\n"), float(input("Enter the Second number!\n"))
ops = {"+": operator.add,   "-": operator.sub,  "*": operator.mul,"/":operator.truediv}
print(f"Your answer is {ops[opp](n1, n2)}!")