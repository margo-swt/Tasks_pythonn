class Animal:
    name = "juggernaut"

    def animal(self):
        print("roar")


class Dog(Animal):
    def dog(self):
        print("woof")

    print(Animal.name)


dog_obj = Dog()
dog_obj.dog()
print(dog_obj.name)
dog_obj.animal()
