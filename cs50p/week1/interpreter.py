expression = input("expression: ").split()
x = float(expression[0])
y = expression[1]
z = float(expression[2])
if y == "+":
 result = x+z
elif y == "-":
 result = x-z
elif y == "/":
 result = x/z
elif y == "*":
 result = x*z
print(f"{result:.1f}")
