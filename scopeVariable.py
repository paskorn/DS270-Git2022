a=10
def func(): 
    global a
    print(a)
    a=5
    print(a)
    
func()
print(a)


