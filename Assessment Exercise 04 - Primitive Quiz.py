# Assessment Exercise 4

class french_city:
    def __init__(self, name):
        self.name = name

fc1 = french_city("Lyon")
fc2 = french_city("Marseille")
fc3 = french_city("Paris")
fc4 = french_city("Orleans")

def fra_capital_question ():
    print("What is the capital of France?")
    print("A. " + fc1.name)
    print("B. " + fc2.name)
    print("C. " + fc3.name)
    print("D. " + fc4.name)

    answer = input("Enter your answer here: ")
    if answer ==  fc1.name:
        print("Wrong answer")
    elif answer == fc2.name:
        print("Wrong answer")
    elif answer == fc3.name:
        print("Correct answer")
    else:
        print("Wrong answer")

fra_capital_question()