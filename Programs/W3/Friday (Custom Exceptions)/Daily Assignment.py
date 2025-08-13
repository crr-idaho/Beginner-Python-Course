class TooMuchData(Exception):
    pass

totData = 0.0

def DataMeasure(data):
    global totData
    totData += data
    if totData > 149.6:
        raise TooMuchData("System overload! Too much data imported into system!")
    else:
        print(f"Total Data: {totData} GB")

while True:
    try:
        DataMeasure(float(input("Enter data import amount (in GB): ")))
    except TooMuchData as e:
        print("ERROR:", e)
        break
    except ValueError:
        print("Enter a valid number.")