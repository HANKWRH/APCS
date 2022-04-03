num = [int(x) for x in input().split()]
d=0
num.sort()
a, b, c = num
print(*num)
if a + b <= c:
    print('No')
    d=1
if d == 0:
    if a**2 + b**2 == c**2:
        print('Right')
    if a**2 + b**2 > c**2:
        print('Acute')
    if a**2 + b**2 <c**2:
        print('Obtuse')
