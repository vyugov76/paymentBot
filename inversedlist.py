a = input()
b = input()
c = input()
d = input()

list = [a, b, c, d]
n = len(list)
res = []

while n >= 0:
    n-=1
    if n<0:
        break
    res.append(list[n])
    
print(res)