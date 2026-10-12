x1_oblast = 4
y1_oblast = 2
x2_oblast = 9
y2_oblast = 7

xb = int(input("Zadejte souřadnici bodu X:"))
yb = int(input("Zadejte souřadnici bodu Y:"))

str1 = xb>=x1_oblast and xb<=x2_oblast and yb==y1_oblast
str2 = yb>=y1_oblast and yb<=y2_oblast and xb==x1_oblast
str4 = yb>=y1_oblast and yb<=y2_oblast and xb==x2_oblast
str3 = xb>=x1_oblast and xb<=x2_oblast and yb==y2_oblast
if str1 or str2 or str3 or str4:
    print(Leží na hranici)
else
    print ("leží mimo hranici")