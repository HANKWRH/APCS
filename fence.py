fence = [int(x) for x in input()]
a = [int(x) for x in input().split()]
c = 0
list_b = []
for i in range(len(a)):
    if  i > 0 and i < (len(a)-1):
        if a[i] == 0:
            list_b.append(min(a[i-1],a[i+1]))
    elif i == 0:
        list_b.append(a[i+1])
    else:
        list_b.append(a[i-1])
for i in range(len(list_b)):
    c += list_b[i]
print(c)
