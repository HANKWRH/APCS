ROWS, COLS = [int(x) for x in input().split()]
a = 1
num = []
list_a = []
for i in range(ROWS):
    row=[int(x) for x in input().split()]
    num.append(max(row))


print(sum(num))
for i in range(len(num)):
    if sum(num)%num[i] == 0:
        list_a.append(num[i])
        a = 0
if a == 1:
    list_a.append('-1')
print(*list_a)
