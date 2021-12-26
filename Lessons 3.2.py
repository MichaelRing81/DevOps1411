my_file = open("read_my_contents.txt")

for line in my_file.readlines():
    print(line, end="")

my_other_file = open("michael.txt", "w")
my_other_file.write("Hey, hey\n")


