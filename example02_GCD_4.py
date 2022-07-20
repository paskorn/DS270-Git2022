def GCD(a,b):
    # Let a always is the least number 
    if (b<a):
        temp=b
        b=a
        a=temp
    i=a
    while (a%i !=0 or b%i !=0):
        i=i-1
    return i

# This is main function
print("Find GCD from two numbers")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("The GCD of ", a," and", b," is ", GCD(a,b) )

