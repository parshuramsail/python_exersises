#program to convert height in feet and inches to centimeters .
print("enter a height?")
feet=float(input("enter a feet:"))
inch=float(input('enter a inch:'))
inch+=feet*12
cm=round(inch*2.54,1)
print("your Height is",cm)
