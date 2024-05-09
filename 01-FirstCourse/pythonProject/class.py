class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        print("Point is drawn")

    def move(self):
        print(f'Point is moved to ' + str(self.x) + ', ' + str(self.y))


p1 = Point(20, 10)
p1.draw()
p1.move()


#---- exercise ---#

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hello, I am {self.name} ")

john = Person("John")
john.talk()