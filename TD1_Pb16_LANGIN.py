def solve(c):
    Sum=0
    chaine=str(c)
    for i in chaine:
        Sum +=int(i)
    return Sum

assert solve(2**15)==26

print(solve(2**1000))