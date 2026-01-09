# Assessment Exercise 6

# 5 password attempts 
attempts = 5
# Loop will run until attempts run out or correct password is entered
while attempts > 0:
    password_input = input("Enter password: ")

    # Loop will run until correct password is entered
    if password_input == "1234":
        print("Correct password")
        break
    else: # Incorrect entries deduct an attempt and display it
        attempts -= 1
        print("You have " + str(attempts) + " attempts left")

# Will run when all password attempts are exhausted
else: 
    print("Maximum attempts reached. Law enforcement have been alerted to your location")
