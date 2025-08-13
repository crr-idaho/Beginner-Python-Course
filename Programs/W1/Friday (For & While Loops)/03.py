# Use a while loop to print even numbers from 2 to 10.
count = 2
countEO = 0

while count <= 200:
    if countEO == 0:
        print(count)
        count += 1
        countEO += 1
    if countEO == 1:
        countEO -= 1
        count += 1
        continue