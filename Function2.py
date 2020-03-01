def person(name,**kwargs):
    print(name)
    print(kwargs)
    for i,j in kwargs.items():
        print(i,j)


person('Hemraj',age=28,place='Shimoga',phone=8095789449)