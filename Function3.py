def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even=even+1
        else:
            odd=odd+1
    return even,odd

lst=[]
n=int(input("Enter numbers:"))
for i in range(n):
    value=int(input("Enter the next value:"))
    lst.append(value)

even,odd=count(lst)
print("Even is:{} and odd is:{}".format(even,odd))