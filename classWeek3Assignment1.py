# ASSIGNMENT 1

"""Create a function that prints our dictionary in a pretty way
 + ask users for items and amounts
 + cover edge cases
 ++ ?
    """
# First dictionary
picnicItems = {'apples': 10, 'oranges': 12, 'flamethrower': 1}

# With this function we can show in an order the picnicItems
def picnic():
    print(" PICNIC ITEMS ".center(26,'*'))
    for key, value in picnicItems.items():
        print(f"{key.ljust(20, '.')} {str(value).rjust(5)}")

# With this function we can add keys and values in picnicItems dictionary
def add_item():
    picnicItems.setdefault(input("Item name: "), int(input("Amount of item: ")))

## With this function we can delete keys and values from picnicItems dictionary    
def del_item():
    del_in = str(input("Select a key name from the list: "))
    del picnicItems[del_in]

#Here we run the functions with the while loop
while True:
    picnic()
    print("What do you want? Choose; 'add', 'delete', 'quit'")
    choice_in = str(input("Write your choice: "))
    if choice_in == 'add':
        add_item()
    if choice_in == 'delete':
        del_item()
    if choice_in == 'quit':
        break
    else: 
        print("\n****Please choose one of the options!**** \n")
        choice_in




