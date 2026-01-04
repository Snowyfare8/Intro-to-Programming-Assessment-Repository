# Assessment Exercise 7

def loop_1():
    for a in range(0, 51, 1):
        print(a)

def loop_2():
    for b in range(50, -1, -1):
        print(b)

def loop_3():
    for c in range(30, 51, 1):
        print(c)

def loop_4():
    for d in range(50, 8, -2):
        print(d)

def loop_5():
    for e in range(100, 201, 5):
        print(e)

def choose_loop_function():
    choose_loop = input("Choose loop to run: ")
    if choose_loop == "1":
        loop_1()
    elif choose_loop == "2":
        loop_2()
    elif choose_loop == "3":
        loop_3()
    elif choose_loop == "4":
        loop_4()
    else: 
        loop_5()

choose_loop_function()