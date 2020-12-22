#SOLUTION 
name  = input("Please enter your name: ")
print(f"Welcome {name}.\ninput type:{type(name)}")

value = int(input("Please enter a value {}:".format(name)))
print("input type:{}".format(type(value)))

sum1 = int(input("Enter a number to sum your value: "))
print(f"Result: {value+sum1}")
print("result type:{}".format(type(value+sum1)))

power = int(input("Enter the power of the your value: "))
print(f"Result: {value**power}\nresult type:{type(value**power)}")

division = float(input("Enter a number to divide your value: "))
print(f"Result: {value/division}")
print("result type:{}".format(type(value/division)))

#SOLUTION(ALTERNATIVE)
"""
value_list = []
for i in range(5):
    values = input(f"Enter a value: ") 
    value_list.append(values) 
print("Your values are {}".format(value_list))
for j in range(len(value_list)):
    try:
        value = int(value_list[j])
        print("Input :{}, is an integer number.\n{}".format(value,type(value)))
    except ValueError:
        try:
            value = float(value_list[j])
            print("Input :{}, is an float number.\ntype:{}".format(value,type(value)))
        except ValueError:
            print(f"Input :{value_list[j]}, is not a number. It's a string\ntype:{type(value_list[j])}")
"""
