def add(a,b):
    c=a+b
    return c
def sub(a,b):
    c=a-b
    return c
def mul(a,b):
    c=a*b
    return c
def div(a,b):
    c=a/b
    return c

print("select operation:")
print("add")
print("sub")
print("mul")
print("div")
value=input("Enter the operation to perform:")
x=int(input("Enter the a value :"))
y=int(input("Enter the b value :"))

if value=='add':
    print(add(x,y))

elif value=='sub':
    print(sub(x,y))
elif value=='mul':
    print(mul(x,y))
else:
    print(div(x,y))




