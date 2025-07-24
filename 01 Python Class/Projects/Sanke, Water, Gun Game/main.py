import random

print("s: for Snake")
print("w: for Water")
print("g: for Gun")

# Computer choice from s, w, g
options = ["s", "w", "g"]
computerStr = random.choice(options)

# User input
youStr = input("Enter Your Choice (s/w/g): ")

# Mapping
youDict = {"s": "Snake", "w": "Water", "g": "Gun"}

print(f"You Chose: {youDict[youStr]} \nComputer Chose: {youDict[computerStr]}")

# Determine winner
if youStr == computerStr:
    print("It's a Draw!")

elif (youStr == "s" and computerStr == "w") or \
     (youStr == "w" and computerStr == "g") or \
     (youStr == "g" and computerStr == "s"):
    print("You Win!")

else:
    print("You Lose!")
