isTrue = False
a = 2
b = 2.5
strOne = "One"
strThree = "Three"

if a >= 2 and strOne == "One" or not strThree == "two":
    print("a is greater than 2")
elif b == 2.5:
    print("something")
else:
    print("a is lower than 2")

a = 3
if 0 < a < 4:
    print("true")

my_list = ["hen", "lior", "shay", "ariel"]
if "hen" in my_list:
    print("yes")
else:
    print("no")

my_other_list = []
if my_other_list:
    print("hello")

if len(my_list) > 0:
    print("hey")

print(len(my_list))

c = 5
d = 5
e = 9
if c is d:
    print("c is d")

if type(e) is int:
    print("e is an integer")

