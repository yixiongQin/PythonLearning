for item in [1,2,3,4,5]:
    print(item)

# output
# 1
# 2
# 3
# 4
# 5


for item in range(10):
    print(item)

for item in range(5,10):
    print(item)

for item in range(5,10,2):
    print(item)

prices = [10, 20, 30]

total = 0
for price in prices:
    total += price
print(f"Total: {total}")
