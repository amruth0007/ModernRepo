class car:
    def __init__(self):
        self.color='white'
        self.model='Hundai'

c1=car()
c2=car()

c2.color='red'
c2.model='Audi'

print(c1.color,c1.model)
print(c2.color,c2.model)