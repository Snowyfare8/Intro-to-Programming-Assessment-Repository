# Assessment 5

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

def month_selection():
    user_input = (str(input("Enter month by number here: ")))
    days = months.get(user_input)
    print(days)

month_selection()