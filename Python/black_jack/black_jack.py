##imposrts
import random
##defntions
suitsdic = {
    0:"clubs",
    1:"dimonds",
    2:"hearts",
    3:"spades"
}
cardvalues = []
altwin = [1,10]
print("These are your cards!")
def draw(n):
    x=0
    while x < n:
        cardnum = random.randint(0,12)
        suitnum = random.randint(0,3)
        suit = suitsdic[suitnum]
        s = open(suit)
        card = s.readlines()
        cardpic = card[cardnum]
        s.close()
        cardvalues.append((cardnum + 1))
        x += 1
        print(cardpic)
        cardvalues.sort()
        cardf1values = [10 for x in cardvalues if x >= 10]
        cardf2values = [x for x in cardvalues if x < 10]
        global score
        global cardfvalues
        cardfvalues = cardf1values + cardf2values
        cardfvalues.sort()
        score = sum(cardfvalues)
draw(2)
score = sum(cardfvalues)
print("You have", score ,"Points")
if score <= 11:
    card3values = [x for x in cardfvalues if x != 1]
    nonone = len(card3values)
    if nonone == 1:
        card3values.append(11)
def inp():
    user = input("Do you want to hit or hold ")
    if user == "hit":
        draw(1)
        print("You have", score, "Points")
    elif user == "hold":
        print("You have", score, "Points")
    else:
        print("invalid input!")
while True:
    if score > 21:
        print("bust")
        exit()
    elif score == 21:
        print("you win")
        exit()
    elif cardfvalues == altwin:
        print("you win")
        exit()
    else:
        inp()