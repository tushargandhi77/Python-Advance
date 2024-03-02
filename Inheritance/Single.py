class Animal:
    def __init__(self,name) -> None:
        self.name = name
    
    def _speak(self):
        pass


class Dog(Animal):
    def __init__(self, name,age) -> None:
        super().__init__(name)
        self.age = age

    def _speak(self):
        return f"{self.name} i am dog and my age is {self.age}"
    

dg = Dog("Mukesh",34)
print(dg._speak())