a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
c=[int(x) for x in input().split()]
d=[int(x) for x in input().split()]
win = 0
lose = 0
a_s=sum(a)
b_s=sum(b)
c_s=sum(c)
d_s=sum(d)
if a_s > b_s:
    win += 1
elif a_s < b_s:
    lose += 1
else:
    pass
if c_s > d_s:
    win += 1
elif c_s < d_s:
    lose += 1
else:
    pass
print(str(a_s)+':'+str(b_s))
print(str(c_s)+':'+str(d_s))
if win > lose:
    
    print('Win')
elif win < lose:
    print('Lose')
else:
    print('Tie')
