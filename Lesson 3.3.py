# try:
#     a = int(input("enter first number: "))
#     b = int(input("enter second number "))
#
#     result = a / b
#     print(result)
#
# except ZeroDivisionError:
#     print("Could not divide by zero")
# except BaseException as e:
#     print("something went wrong" + str(e.args))

def get_user_age():
    age = int(input("enter your age "))
    if age < 0:
        raise ValueError("age can not be negative")

get_user_age()








