# WRITE PROGRAM WHICH WILL KEEP ADDING A NUMBER INPUTED BY THE USER.ADDING STOP AS SOON AS A USER PRESSES A Q IN KEYBOARD.
sum=0
while(True):
    user_input=input(" Enter the item price  or press q to quit :\n")
    if (user_input!="q"):
        sum=sum+int(user_input)
        print(f"your order so far : {sum}")
    else:
        print(f"your bill total is {sum}.Thanks for shopping  with us!")
        break

