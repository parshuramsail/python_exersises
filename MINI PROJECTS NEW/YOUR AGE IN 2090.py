# YOUR AGE IN 2090:Take age or year of birth as an input from the user and tell them when they will turn 100 years old .
# Dont use any ype of modules like date time
# they can than optionally provide a year and your program must tell  their age in that particular year.
# you should be handle all sort of errors  like
# you are not at born
# you seems to be the oldest person alive
# you can handle any other error if possible

yearage=int(input("what is you age / Year of birth : \n"))
isAge=False
isyear=False

if isAge<125:
    isAge=True

elif isAge>1900:
    isyear=True

else:
    print("There was a problem with your age/ Year of birth")
    exit()

