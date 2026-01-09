# Assessment Exercise 7

# Loop from range 0 to 50 in increments of 1
def loop_1():
    for a in range(0, 51, 1):
        print(a)

# Loop from range 50 to 0 in increments of -1
def loop_2():
    for b in range(50, -1, -1):
        print(b)
        
# Loop from range 30 to 50 in increments of 1
def loop_3():
    for c in range(30, 51, 1):
        print(c)

# Loop from range 50 to 8 in increments of -2
def loop_4():
    for d in range(50, 8, -2):
        print(d)

# Loop from range 100 to 200 in increments of 5
def loop_5():
    for e in range(100, 201, 5):
        print(e)

# Allows user to choose which function to run
def choose_loop_function():
    choose_loop = int(input("Choose loop to run: "))
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
