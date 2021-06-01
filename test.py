import random;
chance=4
rn = [1,2,3,4,5,6,7,8,9,10]
rnc = random.choice(rn)
print("Number Guessing Game!")
print("Instructions:")
print("Guess a number between one to ten")
gn = int(input("Guess a number --> "))
while chance>0:
    if gn>rnc:
        print("YOU'RE WRONG. GUESS A NUMBER LESS THAN "+str(gn))
        gn = int(input("Guess a number --> "))
    elif gn<rnc:
        print("YOU'RE WRONG. GUESS A NUMBER MORE THAN "+str(gn))
        gn = int(input("Guess a number --> "))
    elif gn==rnc:
        print("YOU WIN!")
        break
    chance=chance-1

if chance==0:
    print("HAHAHAHAHAHAHA YOU LOSE!\nP.S. You have the worst luck ever")