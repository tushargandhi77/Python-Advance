class Area:
    radius = 0

    def area(self):
        print(f"area of circle:{3.14*self.radius*self.radius}")

a = Area()
a.radius = 5
a.area()