# class Rectangle:
#     def set_params(self, a, b):
#         self.a = a
#         self.b = b
    
#     def calc_surface(self):
#         return self.a * self.b
    
# r = Rectangle()
# r.set_params(5,6)
# print(r.calc_surface())

# class Rectangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def set_params(self, a, b):
#         self.a = a
#         self.b = b
    
#     def calc_surface(self):
#         return self.a * self.b
    
# r = Rectangle(5,6)
# print(r.calc_surface())

# class Rectangle:
#     def __init__(self, a=10, b=6):
#         self.set_params(a, b)

#     def set_params(self, a, par_b):
#         self.a = a
#         self.b = par_b

#     def calc_surface(self):
#         return self.a*self.b

#     def __repr__(self):
#         return "Rectangle[" + str(self.a) + " by " + str(self.b) + "] at " + str(hex(id(self)))


# #r = Rectangle(b=8)
# r = Rectangle()
# r.a = 50
# print(r.calc_surface())
# # destroy r
# del r

# r2 = Rectangle(b=2)
# print(r2)

from copy import copy
# using copy to make 2 different object instead of using = asign variable

