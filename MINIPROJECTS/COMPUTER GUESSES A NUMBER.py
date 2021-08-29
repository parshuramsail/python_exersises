# WRITE PROGRAM TO COMUTER GUESSES YOUR  NUMBER.
# COMPUTER  GUESSES A NUMBER.
# YOU GUIDE COMPUTER TO APPROACH THE ANSWER.
#DONT CHANGE YOUR ANSWER AFTER THE GAME STARTS.

import random
play_game="y"
start=1
end=101
direction="N"
smallest=start
largest=end

while play_game=="y":
    smallest=start
    largest=end
    print("guess a number between 1 to 100")
    try_number=random.randint(start,end)
    print(try_number)
    counter=0
    direction="N"

    while direction!="C":
        direction=input("IS IT TOO LARGE (L),TOO SMALL(S),OR CORRECT(C)?")
        if direction=="S":
            if try_number>smallest:
                smallest=try_number+1
            try_number=random.randint(smallest,largest)
            print(try_number)
        if direction=="L":
            if try_number<largest:
                largest=try_number-1
            try_number=random.randint(smallest,largest)
            print(try_number)
        counter=counter+1
    print("i got it in "+ str(counter) + " times")
    play_game=input("continue?")

