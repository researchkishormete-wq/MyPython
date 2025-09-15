#Write a program to find square roots of the numbers entered
def sqr(num):
    result=num**(1/2)
    return(result)

for i in range(5):
    a=int(input("Enter your number"))
    print("The square root is=",sqr(a))