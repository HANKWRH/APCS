ROCK = 0
SCISSORS = 2
PAPER = 5
WINNING_PLAY_VS = {ROCK: PAPER,
                   PAPER: SCISSORS,
                   SCISSORS: ROCK}
bro = []
# 如果絲絲連續兩輪出了一樣的拳，下一輪他就會出打敗絲絲前兩輪的拳。
# 否則，他下一輪會出跟絲絲前一輪一樣的拳。
F = int(input())#哥出啥0
N = int(input())#妹出拳數
sis = [int(x) for x in input().split()]#妹出拳2

for i in range(N):
    if i > 0:
        if i > 1:
            if sis[i-2] == sis[i-1]:
                F = WINNING_PLAY_VS[sis[i-1]]
        else:
            F = sis[i-1]
    bro.append(F)
    if sis[i] == WINNING_PLAY_VS[F]:
        print(*bro,': Lost at round', i+1)
        break
    elif F == sis[i] and i == N-1:
        print(*bro,': Drew at round', N)
        break
    elif F == WINNING_PLAY_VS[sis[i]]:
        print(*bro,': Won at round', i+1)
        break
