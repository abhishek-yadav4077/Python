m = 1 #global variable

def fn():
    global n
    n = 5 #local variable
    print("in", n)
    print(m)

fn()
print("out", m)
print(n)

#most preference-> local variable

