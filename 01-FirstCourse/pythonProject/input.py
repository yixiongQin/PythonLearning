# ---------- #

name = input(' What is your name? ') # rewrite name with input, add a space at end to make it user friendly

print('Hi ' + name ) # output  What is your name? bear  ; Hi bear

favorite_color = input('What is your favorite color? ') # output What is your favorite color? blue ; blue

print(favorite_color)

# birth_year = input("Enter your birth year: ")
# age = 2019 - birth_year
#
# print(age)
# this will generate error, because the type of input is not `int`
# value type : int, float, string, boolean

birth_year = input("Enter your birthday: ")
print(type(birth_year))
print(birth_year)
age = 2019 - int(birth_year) # int(value) parse the type of value
print(type(age))
print(age)

# output:
# Enter your birthday: 2000
# <class 'str'>
# 2000
# <class 'int'>
# 19

# ------ #

weight_lbs = input("Enter your weight in lbs: ")
weight_kg = int(weight_lbs) * 0.45
print(type(weight_kg))
print(weight_kg)
