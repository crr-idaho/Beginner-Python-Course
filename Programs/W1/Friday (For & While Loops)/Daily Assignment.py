# Generate the first 10 numbers in the Fibonocci sequence.
main_count = 0
seq_step = 0

x = 1
y = 0
z = 0

print(0)
print(1)

while main_count <= 7:
    if seq_step == 0:
        z = y
        y = x
        x = y + z
        print(x)

    if seq_step == 1:
        seq_step = 0
        main_count += 1
        continue

    seq_step += 1