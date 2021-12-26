# A

def my_function(x, y):
    if x > y:
        print("BIG")

    else:
        print("small")


my_function(3, 1)

# B

for i in range(5):
    print(i)

# C

list_of_seasons = [1, 2, 3, 4]

for season in list_of_seasons:
    if season == 1:
        print("summer")
    elif season == 2:
        print("winter")
    elif season == 3:
        print("fall")
    elif season == 4:
        print("spring")


# D

count = 1
while count < 11:
    print(count)
    count = count + 1
# the loop will run 11 times, the last number that will be printer is 10

# E

my_age = 40
first_letter_name = "M"
shekels_dollar_currency = 3.16
flew_abroad = "false"
apartment_number = 8

print(my_age, first_letter_name, shekels_dollar_currency, flew_abroad, apartment_number)
print(my_age + float(shekels_dollar_currency))

# F

phone_number = input("Please enter your phone number ")
print("phone number " + phone_number)


# G

def printHello():
    print("printHello")


printHello()


def calculate():
    print(float(5 + 3.2))


calculate()


# H

def name():
    my_name = input("Please type in your name ")
    print(my_name)


name()


def number():
    my_number = input("Please enter your number ")
    print(int(my_number) / 2)


number()


# I

def method_one():
    first_number = input("please enter the first number: ")
    second_number = input("please enter the second number: ")
    print(int(first_number) + int(second_number))


method_one()


def method_two():
    first_word = input("please enter the first word: ")
    second_word = input("please enter the second word: ")
    print(first_word + " " + second_word)


method_two()


