from sys import stdin
from collections import deque
lines = deque(stdin.readlines())

while lines:
    
    
    ROWS, COLS, _ = [int(x) for x in lines.popleft().split()]
    
    x1 = []

    def rotate(x):
        result = []
        ROWS = len(x)
        COLS = len(x[0])
        for j in range(COLS-1,-1,-1):
            row = []
            for i in range(ROWS):
                row.append(x[i][j])
            result.append(row)
        return result
        
    
    for i in range(ROWS):
        a = [int(x) for x in lines.popleft().split()]
        x1.append(a)
    
    x2 = [int(x) for x in lines.popleft().split()]
    x2.reverse()
    
    for x in x2:
        if x == 1:
            x1.reverse()
        else:
            x1=rotate(x1)
    print(len(x1),len(x1[0]))
    for row in x1:
        print(*row)
