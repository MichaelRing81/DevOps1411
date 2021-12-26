def save_name(name_to_save):
    my_file = open("names.txt", "a")
    my_file.write(name_to_save + "\n")
    my_file.close()

def show_names():
    try:
        my_file = open("names3.txt")
        for name in my_file.readlines():
            print(f"Hello {name}", end="")
        my_file.close()
    except FileNotFoundError as e:
        print("file not found")



for i in range(3):
    save_name((input("Enter your name: ")))
show_names()


#save_name("Ziv")
#save_name("Michael")
#save_name("Murzik")
#show_names()
















