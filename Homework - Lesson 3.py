# 1

#a = 1 / 0


# 2

try:
    a = 1 / 0

except ZeroDivisionError:
    print("Could not divide by zero")


# 3

try:
    x = 1
finally:
    print("finally")

# this code misses the except condition, but it will still run


# 4

# the Except handler won't catch any exception type, because the correct handler name is except


# 5

# Except is not a saved handler name, because python programming is case sensitive


# 6

# except IOError catches the error raised when an input/output operation fails, such as print() and open()
# except ZeroDivisionError catches the error which occurs when a number is divided by a zero


# 7

open("words.txt", "w")


# 8

my_file = open("words.txt", "a")
my_file.write("Michael" + "\n")
my_file.close()


# 9

my_file = open("words.txt", "r")
file_contents = my_file.read()
print(file_contents)
my_file.close()

# 10

my_file = open("words.txt", "a", encoding='utf-8')
my_file.write("מיכאל" + "\n")
file_contents = my_file.read().encode('utf-8')
print(file_contents)
my_file.close()









