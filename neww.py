class Animal:
    def __init__(self, type_: str):
        self.type_ = type_


class Bird:
    def __init__(self,area):
        pass


class Eagle(Animal, Bird):

    def __init__(self, animal_type: str, location: list):
        self.location = location
        # super().__init__(type_=animal_type)
        Animal.__init__(self, type_=animal_type)
        Bird.__init__(self, location)
        
eagle = Eagle(location=["north US", "Austral"], animal_type="Bird")
print(eagle.type_)
print(eagle.location)
eagle[1]



# public, protected, private
class Circle:
    _PI = 3.14

    def __init__(self,radius):
         self.radius = radius

    def _area(self):
            return self._PI * (self.radius ** 2)
    
    def __length(self):
         return 2 * self._PI * self.radius

    def __add__(self, other):
         return Circle(self.radius + other.radius)


a = "12"
b = "34"

# a + b -> "1234"
# a.__add__(b)


c_1 = Circle(10)
c_2 = Circle(20)


print(c_1._area())
# print(c_1.__length())
c_1._PI = 5
print(c_1._PI)


# c_1 + c_2 -> c + c_3
c_1.__add__(c_2)
print(c_1 + c_2)