while True:
    if input("Add new entry? ").lower() in ["yes", "y", "yeah"]:
        with open ("entries.txt", "a") as f:
            entry = input("Enter entry: ").strip()
            if entry:
                f.write(entry + "\n")
            else:
                print("Empty entry not saved.")
    else:
        print("Goodbye")
        break