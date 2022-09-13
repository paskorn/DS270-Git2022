a=8
b=2
def func(): 
    global a
    print(a)
    a=5
    print(a)
    b=5
    
func()
print(a)
print(b)

