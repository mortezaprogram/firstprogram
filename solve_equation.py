def solve(equation):
    x, op1, y, op2, r=equation.split()
    y,r=int(y),int(r)
    return "x = " + str(r - y)
print(solve("x + 10 = 65"))