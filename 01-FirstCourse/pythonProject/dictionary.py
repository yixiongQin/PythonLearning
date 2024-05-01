customer = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'is_verified': True
}

customer['first_name'] = "Teddy Bear"
customer['birthdate'] = "1999-12-12"
print(customer.get('birthdate'))


# ----- exercise ----- #

phone = input("Phone: ")
numbers = {
    'number1' : "one",
    'number2' : "two",
    'number3' : "three",
    'number4' : "four",
    'number5' : "five",
    'number6' : "six",
    'number7' : "seven",
    'number8' : "eight",
    'number9' : "nine",
    'number0' : "zero",
}
output = ""
for ch in phone:
    output += numbers.get(f"number{ch}", "!") + " "

print(output)