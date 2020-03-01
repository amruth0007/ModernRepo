import array as arr
array1=arr.array('i',[2,5,9,7,10])   #actual syntax of array

newarr=arr.array(array1.typecode,(a*2 for a in array1))
for a in newarr:
    print(a)