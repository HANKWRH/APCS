n, d = [int(x) for x in input().split()]

list_a = []
e=0
money = 0
for _ in range(n):
    num = [int(x) for x in input().split()]
    num.sort()
    if num[2]-num[0]>=d:
        money = money + (num[0]+num[1]+num[2])/3
        e=e+1
    else:
        pass

list_a.append(e)
print(*list_a,int(money))
