# WRITE CODE FOR GUESS GAME.
import random
play_game='y'
while (play_game=='y'):
    answer=random.randint(1,100)
    try_number=int(input("ENTER A NUMBER BETWEEN 0 AND 100:"))
    count=1
    while try_number!=answer:
        if try_number>answer:
            print("YOUR NUMBER IS TOO LARGE")
        if try_number<answer:
            print('YOUR NUMBER IS TOO SMALL')
        try_number=int(input("ENTER A NUMBER BETWEEN 0 AND 100:"))
        count+=1
    print("YOU GOT IT! YOU TRIED IT IN ", str(count)," TIMES")



