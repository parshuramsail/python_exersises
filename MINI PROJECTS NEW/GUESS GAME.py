# PROGRAM TO SELECT CAR NUMBER PLATE.
car_plates=["AB1234","CD5678","EF901","GH234","JK567","LM8901"]
odd_day=["MO","WE","FR"]
even_day=["TU","TH","SA"]
pass_list=[]
today=input("enter a day of week(SUNDAY TO SATURDAY):")
for plate in car_plates:
    last_digit=int(plate[-1])
    if today in odd_day and last_digit %2!=0:
        pass_list.append(plate)

    elif today in even_day and last_digit %2 ==0:
        pass_list.append(plate)

    elif today== "SU":
        pass_list.append(plate)
print(*pass_list,sep='\n')
