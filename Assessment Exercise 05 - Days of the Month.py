# Assessment 5

# Asks user for month from 1-12 (Jan-Dec)
def month_selection():

# Dictionary of months and their respective days

    months = {
    "1":31, 
    "2":28, 
    "3":31, 
    "4":30, 
    "5":31, 
    "6":30, 
    "7":31, 
    "8":31, 
    "9":30,
    "10":30, 
    "11":30, 
    "12":31
    }

    user_input = str(input("Enter month by number here: "))
    # Activates if user inputs 2 (Feb)
    if user_input == "2":
        # Asks if current year is a leap year
        leap_year_question = str(input("Leap year? ")).lower()
        if leap_year_question == "yes": # Adds an additional day to Feb if yes
            months["2"] = 29
            days = months.get(user_input)
            print(days)
        else: # No additional day to Feb if not
            leap_year_question == "no"
            days = months.get(user_input)
            print(days)
    else:
        user_input != "2"
        days = months.get(user_input)
        print(days)

month_selection()
