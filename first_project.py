#Validate username exercise
#1. Username no more than 12 characters
#2. Username must not contain spaces
#3. Username must not contain digits

username= input("Enter Username")
user_space= username.find("")
number_username= len(username)
is_alpha= username.isalpha()
#print(is_alpha)
#print(user_space)
#print(number_username)

if number_username != 12:
    print("Username must not be less/more than 12 characters")
elif user_space== 1:
    print ("Username must not contain spaces")
elif is_alpha== False:
    print("Username must contain only alphabet")
else:
    print(f"Welcome {username}")