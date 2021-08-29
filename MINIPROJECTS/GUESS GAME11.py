import random
play_game="y"
while (play_game=="y"):
    answer=random.randint(0,100)
    try_number=int(input("enter a number:"))
    count=1
    while try_number!=answer:
        if try_number>answer:
            print(" you enterd to large number")
        if try_number<answer:
            print("you eneterd too small number")
        try_number=int(input("enter a number:"))
        count+=1
    print("you got it! you tried it in ",str(count),"times")
