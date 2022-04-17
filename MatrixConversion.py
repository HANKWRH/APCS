b = [int(x) for x in input().split()]
ROWS = b[0]
COLS = b[1]
x1 = []
x2 = []
def rotate():
    for i in range(ROWS):
        pass
    

for i in range(ROWS):
    a = [int(x) for x in input().split()]
    x1.append(a)
x1.reverse()
print(x1)

for i in range(b[2]):
    c = [int(x) for x in input().split()]
    x2.append(c)
for i in range(len(x2)):
    if x2[i] == 1:
        x1.reverse()
    else:
        x1.rotate()
