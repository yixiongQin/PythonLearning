##
# = , ==, >=, <, <=
# equal should use `==` instead of `=`#

temperature = 35

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")


# -- exercise --#
name = "Teddy Bear"

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be at most 50 characters")
else:
    print("name looks good")