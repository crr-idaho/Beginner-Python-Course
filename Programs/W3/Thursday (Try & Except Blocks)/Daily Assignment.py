import csv
x = 0

try:
    with open ("C:/Users/itzco/Downloads/sample_users.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if x > 0:
                print("Name|" + row[0])
                print("Age|" + row[1])
                print("Email|" + row[2] + "\n")
            x += 1
except Exception as e:
    print(f"Error: {e}")