import array as arr
newarr=arr.array('i',[])
n=int(input("Enter the number of values you want : "))
for i in range(n):
    val=int(input("Enter the next value : "))
    newarr.append(val)
for a in newarr:
    print(a)

search=int(input("Enter the value to search from array : "))
for e in newarr:
    if search==e:
        print(newarr.index(e))
        break
