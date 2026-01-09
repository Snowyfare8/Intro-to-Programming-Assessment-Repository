# Assessment Exercise 4

# Create class "french_city"
class french_city:
    def __init__(self, name):
        self.name = name

# Define four variables cities to be used later
fc1 = french_city("Lyon")
fc2 = french_city("Marseille")
fc3 = french_city("Paris")
fc4 = french_city("Orleans")

# Create question and answer function
def fra_capital_question ():
    print("What is the capital of France?")
    print("A. " + fc1.name)
    print("B. " + fc2.name)
    print("C. " + fc3.name)
    print("D. " + fc4.name)

    # Capitalizes users answers, such that the system recognizes the user's answer as being capitalized regardless of initial input
    answer = input("Enter your answer here: ").capitalize() 
    if answer ==  fc1.name:
        print("Wrong answer")
    elif answer == fc2.name:
        print("Wrong answer")
    elif answer == fc3.name:
        print("Correct answer")
    else:
        print("Wrong answer")

# Call function
fra_capital_question()
