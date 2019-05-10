def basic():
    for a in range(0, 151):
        print(a)

def multiples():
    for b in range(5, 1001, 5):
        print(b)

def counting():
    for c in range(1, 101):
        if c % 10 == 0:    
            print("Coding Dojo")
        elif c % 5 == 0:
            print("Coding")
        else:
            print(c)

def whoa():
    p = 0
    for c in range(0, 500000):
        p = c+p
        print(p)

def countdown():
    for d in range(2018, 0, -4):
        print(d)

def flexcount(lowNum, highNum, mult):
    for e in range(lowNum, highNum, mult):
        print(e+1)

flexcount(2, 9, 3)