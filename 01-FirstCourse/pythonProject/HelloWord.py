print("Hello World")
print("Dog")
print('o----')
print(' ||||')
print('*' * 10)


import module
from module import lbs_to_kg

print(module.lbs_to_kg(30))

numbers = [10,20,30,40,50,60,70,80,90]
module.find_max(numbers)
print(module.find_max(numbers))

# import ecommerce.shipping
# ecommerce.shipping.calc_shipping()

from ecommerce.shipping import calc_shipping
print(calc_shipping())
