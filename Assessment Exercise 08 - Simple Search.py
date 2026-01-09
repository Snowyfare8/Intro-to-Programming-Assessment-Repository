# Assessment Exercise 8

# Define name list
name_list = {
    "Jake",
    "Zac",
    "Ian",
    "Ron",
    "Sam",
    "Dave"
}

# Function to search for name
def name_search():
    # Function to create user input
    search_input = input("Input name here: ").capitalize()
    if search_input in name_list:
        print("name found")
    else:
        print("name not found")

# Calls "name_search" function
name_search()

