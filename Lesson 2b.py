what_to_print = "hello world!"


print(what_to_print * 4)

print(list(range(5)))

print(list(range(9, 2, -1)))

amounts_of_prints = 4

for i in range(amounts_of_prints):
    print(what_to_print)

list_of_names = ["michael", "noam", "lior", "amichai"]

for i in range(1, amounts_of_prints):
    print(str(i)) + ") " + what_to_print

for i in range(len(list_of_names)):
    print(list_of_names[i])

for name in list_of_names:
    print(name)

for name in list_of_names:
    if name == "hen":
        continue

for name in list_of_names:
    if name == "hen":
        break








