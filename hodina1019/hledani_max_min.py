print("zadejte postupně x y z")
x = int(input())
y = int(input())
z = int(input())
max = x
if y >= max:
    max = y
    min = x
else:
    min = y
if z < min and not z > max:
    min = z
else:
    max = z
    if max < x:
        max = x
print("Minimum je " + str(min))
print("Maximum je " + str(max))
