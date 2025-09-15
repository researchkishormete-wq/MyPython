#Function to test if number is prime
def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for i in range(2,n):
            if(n % i==0):
                return False
        return True

num=int(input("Enter a Number "))
if test_prime(num):
    print("Num ", num , "is Prime")
else :
    print("Num ", num , "is NOT Prime")