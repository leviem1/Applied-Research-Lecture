bag = ["D", "D", "N", "N", "G", "P"]  # The coins that we have
coinNumber = 0  # To keep track of which coin we're looking at

# total variable
total = 0.0

# loop
while coinNumber < len(bag):
    theCoin = bag[coinNumber]

    if theCoin == "N":
        total = total + .05
    elif theCoin == "D":
        total = total + .10
    elif theCoin == "Q":
        total = total + .25
    elif theCoin == "G":
        total = total + 1.00
    elif theCoin == "P":
        total = total + .01

    coinNumber = coinNumber + 1

print(total)
