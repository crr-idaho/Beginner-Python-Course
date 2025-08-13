pb = {}

print("\nWelcome to your personal phone book.")

while True:
    print("\nEnter a number to continue.")
    print("1: Add a contact")
    print("2: Look up contact")
    print("3: Display all contacts")
    print("Or type 'done' to quit.")
    ui = input("Your choice: ")

    if ui == "1":
        while True:
            print("\nAdding new contact...")
            con_name = input("Contact name: ")
            con_num = input("Contact number: ")
            pb[con_name] = con_num
            print(f"Added new contact: {con_name} → {con_num}")

            again = input("Add another? (Y/N): ").lower()
            if again != "y":
                break

    elif ui == "2":
        lu_name = input("\nContact name: ")
        print(pb.get(lu_name, "Contact not found."))

    elif ui == "3":
        if pb:
            print("\nAll contacts:")
            for name, number in pb.items():
                print(f"{name}: {number}")
        else:
            print("Phone book is empty.")

    elif ui.lower() == "done":
        print("Goodbye!")
        break

    else:
        print("ERR: INVALID INPUT")