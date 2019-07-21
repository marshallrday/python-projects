import random

cpunum = random.randint(0, 2)
usernum = int(input("We are going to play rock paper scissors. Enter 0 for scissors, 1 for rock, or 2 for paper: "))

if cpunum == 0:
    cpucode = 'Scissors'
elif cpunum == 1:
    cpucode = 'Rock'
elif cpunum == 2:
    cpucode = 'Paper'

if usernum == 0:
    usercode = 'Scissors'
elif usernum == 1:
    usercode = 'Rock'
elif usernum == 2:
    usercode = 'Paper'

print("You chose: ", usercode)
print("The CPU chose: ", cpucode)

if usernum == cpunum:
    print("it's a draw")

if ((usernum == 0 and cpunum == 1) or
        (usernum == 1 and cpunum == 2) or
        (usernum == 2 and cpunum == 0)):
    print("cpu wins:(")

if ((usernum == 1 and cpunum == 0) or
        (usernum == 2 and cpunum == 1) or
        (usernum == 0 and cpunum == 2)):
    print("You win!")
