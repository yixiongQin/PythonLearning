names = ['John', 'Bob', 'Dave', 'Eve']
print(names[-2]) # output: Dave
print(names[2 : 4]) # output: ['Dave', 'Eve']

# ---- largest number ----#

numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)


numbers.insert(0, 10)
print(numbers) # [10, 3, 6, 2, 8, 4, 10]

numbers.remove(10)
print(numbers) # [3, 6, 2, 8, 4, 10]

numbers.pop(5)
print(numbers) # [3, 6, 2, 8, 4]

numbers.sort()
print(numbers) # [2, 3, 4, 6, 8]

numbers.reverse()
print(numbers) # [8, 6, 4, 3, 2]


# ---- exercise ----- #

numbers1 = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []

for number in numbers1:
    if number not in uniques:
        uniques.append(number)
print(uniques) # [2, 4, 6, 3, 1]


# ----------- #

numbers2 = (1, 2, 3)
numbers2[0]
print(numbers2[0]) # cannot modify

coordinates = (1, 2, 3)
x, y, z = coordinates
print(y) # unpacked