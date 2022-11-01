a = input("Enter side lengths ")
digits = ["0","1","2","3","4","5","6","7","8","9"]
for i in range(len(a)):
  if a[i] in digits:
    continue
  else:
    b = float(a[:i])
    break
x=i
for i in range(x+1,len(a)):
  if a[i] in digits:
    continue
  else:
    c = float(a[x+1:i])
    break

d = float(a[i+1:len(a)])
s = (b+c+d)/2
area = (s*(s-b)*(s-c)*(s-d))**0.5
print("area = " + str(area))