# Tresure island
print("Welcome to treasure island")
input1 = input("Where do you wanna go 'Left' or 'right'")
alpha = input1.lower()
if alpha == "left":
    print("Sorry !!! you lost")
else:
    print("You have reached to a coast")
    
input2 = input("Do you wanna 'wait' for a boat or 'swim' across")
beta = input2.lower()
if beta == "swim": 
    print("Sorry !!! crocrodile ate you game over.")
else:
    print("You have reached to an island")

input3 = input ("you have three doors infront of you 'Red', 'yellow' and 'Blue'")
gama = input3.lower()
if gama == "red":
    print("Dragon ate you game over, Better luck next time")
elif gama == "Yellow":
    print("you fall in a mud pool, Game OVER")
else:
    print("You won!!!")