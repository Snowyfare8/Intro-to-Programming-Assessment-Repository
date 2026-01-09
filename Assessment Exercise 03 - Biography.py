# Assessment Exercise 3

# Blank biographical dictionary
bio_info = {

}

# Asks for user input 
name_input = str(input("Input your name here: ")) # Creates one continous name string e.g. Abdulaziz Tejada
hometown_input = str(input("Input your hometown here: ")) # Value must be string
age_input = int(input("Input your age here: ")) # Value must be integer

# Updates dictionary "bio_info"
bio_info.update({"name":name_input})
bio_info.update({"hometown":hometown_input})
bio_info.update({"age":age_input})
# Prints dictionary "bio_info"
print(bio_info)
