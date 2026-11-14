input_month = input()
input_day = int(input())

if input_month == "January" and (1 <= input_day <= 31):
    print("Winter")
elif input_month == "February" and (1 <= input_day <= 28):
    print("Winter")
elif input_month == "March" and (1 <= input_day <= 31):
    if input_day < 20:
        print("Winter")
    else:
        print("Spring")
elif input_month == "April" and (1 <= input_day <= 30):
    print("Spring")
elif input_month == "May" and (1 <= input_day <= 31):
    print("Spring")
elif input_month == "June" and (1 <= input_day <= 30):
    if input_day < 21:
        print("Spring")
    else:
        print("Summer")
elif input_month == "July" and (1 <= input_day <= 31):
    print("Summer")
elif input_month == "August" and (1 <= input_day <= 31):
    print("Summer")
elif input_month == "September" and (1 <= input_day <= 30):
    if input_day < 22:
        print("Summer")
    else:
        print("Autumn")
elif input_month == "October" and (1 <= input_day <= 31):
    print("Autumn")
elif input_month == "November" and (1 <= input_day <= 30):
    print("Autumn")
elif input_month == "December" and (1 <= input_day <= 31):
    if input_day < 21:
        print("Autumn")
    else:
        print("Winter")
else:
    print("Invalid")
    
# input_month = input()
# input_day = int(input())

# if input_month == "April":
#     print("Spring")
# elif input_month == "May":
#     print("Spring")

# if input_month == "March":
#     if input_day < 20:
#         print("Winter")
#     elif input_day >= 20:
#         print("Spring")
#     elif input_day > 20:
#         print("Spring")
#     elif input_month == "January":
#         if input_day >= 1 and input_day <= 31:
#             print("Winter")
#     elif input_month == "February":
#         if input_day >= 1 and input_day <= 28:
#             print("Winter")
   
# if input_month == "June":
#     if input_day >= 21:
#         print("Summer")
#     elif input_day < 21:
#         print("Spring")
#     elif input_month == "July":
#         print("Summer")
#     elif input_month == "August":
#         print("Summer")
    
# if input_month == "September":
#     if input_day >= 22:
#         print("Autumn")
#     elif input_day < 22:
#         print("Summer")
#     elif input_month == "October":
#         print("Autumn")
#     elif input_month == "November":
#         print("Autumn")
  
# if input_month == "December":
#     if input_day > 21:
#         print("Winter")
#     elif input_day < 21:
#         print("Autumn")
# else:
#     print("Invalid")


