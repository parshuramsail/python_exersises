# write program to find the factorial of a given number.and number of trailing zeros in that factorial.
def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*int(factorial(num-1))
def  fact_zeros(num):
    count=0
    i=5
    while(num//i !=0):
        count+=int(num/i)
        i=i*5
        return count
if __name__=="__main__":
    num=int(input("enter a number:"))
    print(fact_zeros(num))

