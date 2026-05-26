name = input("camel case:")
result = ""
for char in name:
    if char.isupper():
        result = result + "_" + char.lower()
    else:
        result = result + char

print(result)

