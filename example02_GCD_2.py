print("Find GCD from two numbers")
a = int(input("Enter a: "))
b = int(input("Enter b: "))

# Let a always is the least number 
if (b<a):
    temp=b
    b=a
    a=temp

print("a =", a, "b =",b)

for i in range(a,2,-1):
    if (a%i ==0 and b%i==0):
        answer =i
        break
    
print("The GCD of ", a," and", b," is ", answer )


