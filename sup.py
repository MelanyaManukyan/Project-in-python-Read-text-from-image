# class ValueTooSmallError(ValueError):
#     def __init__(self, message):
#         super().__init__(message)

# # class ValueTooSmallError(ValueError):
# #     def __str__(self):
# #         return "string lenght should be greater than 6"
    

# text = "hi"
# if len(text) < 6:
#         raise ValueTooSmallError("var text lenght less than 6")







# class Rectangle:
#      def __init__(self, height, width):
#           self.height = height
#           self.width = width

#      def area(self):
#           return self.height * self.width
     
#      @staticmethod
#      def static_area(height, width):
#           return height * widht
     
# class Ball:
#      def __init__(self, radius):
#           self.radius = radius

#      @staticmethod
#      def main_circle_area(radius):
#           return 3.14 * (radius ** 2)
     
# class Circle:
#      def __init__(self, radius):
#           self.radius = radius
     

#      def area(self):
#           return Ball.main_circle_area(self.radius)
     



class Room:
     def __init__(self, lenght, width, height):
          self.__lenght = lenght
          self.__width = width
          self.__height = height
          
          @property
          def width(self):
               return self.__width
          
          @width.setter
          def width(self, value):
               if value > 1:
                    self.__width = value
               else:
                    raise ValueError
               
room_1 = Room(10, 10, 10)
room_1.width = 3
print(room_1.width)

               



