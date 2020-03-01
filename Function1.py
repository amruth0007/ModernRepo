def person(name,age):
    print(name)
    print(age)

def sum(a,*b):
    c=a
    print(b)
    for i in b:
        c=c+i
    print(c)

sum(20,10,30,40)