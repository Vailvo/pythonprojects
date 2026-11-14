import datetime
# importing datetime so that it is current with each year
current_year = datetime.date.today().year
# setting the variable of current_year to be datetime to 
# fetch current year dynamically from the system date
username = input("Please enter your name:\n")
# By using input function I retrieved the user's name
user_age = int(input("Please enter your age:\n"))
# Retrieved the user_age setting it to the int() function while nesting in the input()
birth_year = current_year - user_age
# birth_year is set to equal current year subtracted from the user_age
print(username, "you were born in", birth_year)
# It is then printed that output of the input of the username with the string 
# and with the birth_year