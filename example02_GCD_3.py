print("Find GCD from two numbers")
a = int(input("Enter a: "))
b = int(input("Enter b: "))

# Let a always is the least number 
if (b<a):
    temp=b
    b=a
    a=temp

print("a =", a, "b =",b)

i=a
while (a%i !=0 or b%i !=0):
        i=i-1

answer =i
        
    
print("The GCD of ", a," and", b," is ", answer )


