course = 'Python for "Beginners"' # quote is sensitive
print(course) # output: Python for "Beginners"

# -------- #

course = '''
Hi Bear,

Hear is our first email to you.

Thank you.
The support team
'''

print(course)

course = 'Python for Beginners' # just for reset
print(course[0]) # output: 'P'. not available for other language

print(course[-2]) # output: 'r'

print(course[0:3]) # output: 'Pyt'

print(course[2:]) # output: 'thon for Beginners'. from 2 to the end by default(0)

name = 'Jennifer'
print(name[1:-1]) # output: 'ennife'

# ---------- #

first = 'John'
last = 'Doe'
message = first + ' [' + last + '] is a coder' # is not use friendly
msg = f'{first} [{last}] is a coder' # start with f'' to format message
print(message)
print(msg) # John [Doe] is a coder

# ---------- #
print(course) # output: 'Python for Beginners'
print(len(course)) # output: 20

print(course.upper()) # output:`PYTHON FOR BEGINNERS`

print(course.find('o')) # output: 4.  index of char 'o'

print(course.find('O')) # output: -1. false, since no 'O' in the string

print(course.replace('P', 'J')) # output: `Jython for Beginners`

print('Python' in course) # output: True. a boolean function

# len(), upper(), lower(), title(), find(), replace(), in


