# Create a phone book app using a dictionary
pb = {}
entry_pb = {}

print("\nWelcome to your personal phone book.")

while True:
    print("Enter a number to continue.")
    print("\n1: Add a contact")
    print("2: Look up contact")
    print("3: Display all contacts")
    print("Or type done to quit.")
    ui = input("")

    # Adding a contact
    if ui == "1":
        while True:
            print("\nAdding new contact...")
            con_name = input("Contact name: ")
            con_num = input("Contact number: ")
            entry_pb[con_name] = con_num
            pb.update(entry_pb)
            print("Added new contact:", entry_pb)
            entry_pb.clear()
            print("\nAdd another? Y/N:")
            ui1 = input("")
            if ui1.lower() == "y":
                continue
            elif ui1.lower() == "n":
                break
            else:
                print("ERR: INVALID INPUT")
                break

    # Looking up a contact
    elif ui == "2":
        lu_name = input("\nContact name: ")
        print(pb[lu_name])

    # Display all contacts
    elif ui == "3":
        print(pb)

    # Close phonebook
    elif ui == "done":
        break

    # Handles invalid inputs
    else:
        print("ERR: INVALID INPUT")
        continue