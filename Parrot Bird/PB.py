class Parrot:
    species="Bird"
    def __init__(self,name,color,age):
        self.name=name
        self.age=age
        self.color=color
blu=Parrot("Blu",10,"Green")
woo=Parrot("Woo",15,"Red")
print(blu.name)
print(blu.age)
print(blu.color)
print(woo.name)
print(woo.age)
print(woo.color)