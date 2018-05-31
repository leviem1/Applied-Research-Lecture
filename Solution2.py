bag = ["D", "D", "N", "N", "G", "P"]  # The coins that we have
coinNumber = 0                        # To keep track of which coin we're looking at
dimes = 0
nickles = 0
pennies = 0
dollars = 0

# Loop
while coinNumber < len(bag):
    theCoin = bag[coinNumber]

    if theCoin == "D":
        dimes = dimes + 1
    elif theCoin == "N":
        nickles = nickles + 1
    elif theCoin == "P":
        pennies = pennies + 1
    elif theCoin == "G":
        dollars = dollars + 1

    coinNumber = coinNumber + 1         # Look at next coin

total = dimes * .10 + nickles * .05 + pennies * .01 + dollars * 1.0

# Display total
print(total)
