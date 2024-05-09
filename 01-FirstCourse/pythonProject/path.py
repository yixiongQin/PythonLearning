from pathlib import Path

# Absolute path
# path = Path("ecommerce1")
# print(path.exists()) # False
# print(path.mkdir())

path = Path()
for file in path.glob('*.py'):
    print(file)

# Relative path