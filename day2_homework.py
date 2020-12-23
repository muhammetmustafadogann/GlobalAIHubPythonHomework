user = []
fname =input("Enter your first name: ")
lname = input("Enter your last name: ")
age = int(input("Enter your age: "))
year = int(input("Enter your date of birth as year: "))
for i in range(1):
    user.extend([fname,lname,age,year])
    print('-'*30)
    print(f"USER INFO\nName:{user[0]}\nLast Name:{user[1]}\nAge:{user[2]}\nBirth Year:{user[3]}")
    if age <= 0 or year < 1850:
        print("Please enter a valid age or birth date.")
    elif age < 18:
        print("You can not go out because it's too dangerous.")
    else:
        print("You can go out to the street")
