def wish():
    print("Hello Good eve")

def add(x,y):
    z=x+y
    print(z)

def sub(a,b):
    c=a-b
    print(c)

def add_sub(a,b):
    c=a+b
    d=a-b
    return c,d

result1,result2=add_sub(25,3)
print(result1,result2)