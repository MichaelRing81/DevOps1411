my_number = "4"
result = int(my_number) - 2
print(result)

my_number = "4"
result = float(my_number) - 2
print("your result is " + str(result))
print(f"your result is {result - 1.5}")

my_list = [1, 2, 3, 4]
print(my_list[4:0:-1])

my_dict = {"fname": "Ring", "lname": "Michael", "age": 40, "id": 307555896}
key_to_print = input(f"enter key: {list(my_dict.keys())}: ")
print("you choose to print: " + str(my_dict[key_to_print]))








