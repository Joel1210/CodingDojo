print("1.")
def a():
    return 5
print(a())

print("2.")
def b():
    return 5
print(b()+b())

print("3.")
def c():
    return 5
    return 10
print(c())

print("4.")
def d():
    return 5
    print(10)
print(d())

print("5.")
def e():
    print(5)
x = e()
print(x)

print("6.")
def f(b,c):
    print(b+c)
print(f(1,2) + f(2,3))

print("7.")
def g(b,c):
    return str(b)+str(c)
print(g(2,5))

print("8.")
def h():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(h())

print("9.")
def i(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(i(2,3))
print(i(5,3))
print(i(2,3) + i(5,3))

print("10.")
def j(b,c):
    return b+c
    return 10
print(j(3,5))

print("11.")
b = 500
print(b)
def k():
    b = 300
    print(b)
print(b)
k()
print(b)

print("12.")
b = 500
print(b)
def l():
    b = 300
    print(b)
    return b
print(b)
l()
print(b)

print("13.")
b = 500
print(b)
def m():
    b = 300
    print(b)
    return b
print(b)
b=m()
print(b)

print("14")
def n():
    print(1)
    o()
    print(2)
def o():
    print(3)
n()

print("15.")
def p():
    print(1)
    x = q()
    print(x)
    return 10
def q():
    print(3)
    return 5
y = p()
print(y)