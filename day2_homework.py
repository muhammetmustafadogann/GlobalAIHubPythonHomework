user = []
for i in range(1):
    fname =input("Enter your first name: ")
    lname = input("Enter your last name: ")
    age = int(input("Enter your age: "))
    year = int(input("Enter your date of birth as year: "))
    user.extend([fname,lname,age,year])
    if age <= 0 or year < 1850:
        print("Please enter valid age.")
    elif age < 18:
        print("You can not go out because it's too dangerous.")
    else:
        print("You can go out to the street")
print(user)