from random import randint

colors={
    "1":"blue",
    "2":"red",
    "3":"green",
    "4":"yellow",
    "5":"purple",
    "6":"orange",
    "7":"pink",
    "8":"white",
    "9":"black",
    "10":"brown"
}

initial=[]
while len(initial)<4:
    color=colors[str(randint(1, 10))]
    if color not in initial:
        initial.append(color)
for i in range(1,5):
    print("you have %s attempts left"%(5-i))
    white = 0
    black = 0
    guess = input().split(',')
    for item in guess:
        if item in initial:
            white+=1
    for j in range(0,4):
        if guess[j]==initial[j]:
            black+=1
    if black==4:
        print("you won!")
        break
    else:
        print("you lose!")
        print("black:%s\t white:%s"%(black,white))
