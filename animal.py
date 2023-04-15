class Animal:
    def __init__(self, type_: str):
        self.type_ = type_




class Eagle(Animal):

    def __init__(self, animal_type: str, location: list):
        self.location = location
        super().__init__(type_=animal_type)
        # Animal.__init__(self, type_=animal_type)
        
    def __getattribute__(self, location):
        self.location


eagle = Eagle(location=["north US", "Austral"], animal_type="Bird")
print(eagle.type_)
print(eagle.location)
print(eagle[1])
eagle[1] = "EUR"
print(eagle[1])
print(eagle.location)


#  a class esim inch 
a = A()
result = a(1)(2)(3)(4)(5)
print(result)  # should be 15


