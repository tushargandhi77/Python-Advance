class Area:
    def __init__(self,len,bred) -> None:
        self.len = len
        self.bred = bred

    def area(self):
        print("The area of rectange: {}".format(self.len*self.bred))

a = Area(3,5)
a.area()
