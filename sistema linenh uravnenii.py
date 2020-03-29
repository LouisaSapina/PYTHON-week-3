a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
d = float(input("d="))
e = float(input("e="))
f = float(input("f="))

z=(d * a - b * c)
if z == 0 or a ==0 :
                print ("нет решения")
else:
              y = ((f * a - e * c) / (d * a - b * c))
x = ((e - b * y) / a)
print(x, y)
