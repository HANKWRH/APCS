input()
a = [int(x) for x in input().split()]
a.sort()
for i in range(len(a)):
    if a[i]>=60:
        print(a[i])
        print(a[i-1])
    elif a[-1]<60:
        print('worst case')
        print(a[-1])
    if a[0]>=60:
        print('best case')
        print(a[0])
    
