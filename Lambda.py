from functools import *
nums=[10,15,20,25,30,35]
even=list(filter(lambda n:n%2!=0,nums))  # lambda input:expression
double=list(map(lambda a:a*2,even))      #map takes only one input variable
sum=reduce(lambda a,b:a*b,double)        #reduce takes two input variabe from same list
print(even)
print(double)
print(sum)
