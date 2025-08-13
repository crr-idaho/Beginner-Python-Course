#UNFINISHED, skipped due to repeat material

inventory = {
    "notebook": {
        "quantity": 40,
        "price": 2.50
    },
    "pencil" : {
        "quantity" : 100,
        "price" : 0.50
    },
    "usb drive": {
        "quantity": 25,
        "price": 8.99
    },
    "mouse pad": {
        "quantity": 30,
        "price": 3.75
    },
    "water bottle": {
        "quantity": 15,
        "price": 12.00
    },
    "headphones": {
        "quantity": 10,
        "price": 45.00
    },
    "stapler": {
        "quantity": 12,
        "price": 6.25
    },
    "backpack": {
        "quantity": 8,
        "price": 55.00
    },
    "charger": {
        "quantity": 20,
        "price": 18.99
    },
    "blue pen": {
        "quantity": 200,
        "price": 0.75
    },
}

def add_item():
    i_n = input("ENTER ITEM NAME: ")
    i_p = input("ENTER ITEM PRICE: ")
    i_q = input("ENTER ITEM QUANTITY: ")

def remove_item():
    i_n = input("ENTER ITEM NAME: ")

def view_inventory():
    print(inventory)

while True:
    print("WELCOME TO COLLEGE NEEDS STOP-N-SHOP INVENTORY SYSTEM")
    user_com = input("(1)VIEW INVENTORY\n(2)ADD AN ITEM\n(3)REMOVE AN ITEM\n(3)EDIT AN ITEM\n(4)EXIT\nENTER COMMAND: ")
    if user_com == "1":
        view_inventory()
    elif user_com == "2":
        add_item()
    elif user_com == "3":
        remove_item()
    elif user_com == "4":
        break
    else:
        print()