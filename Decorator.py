def div(a,b):
    c=a/b
    print(c)

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

div1=smart_div(div)
div1(5,10)