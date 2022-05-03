CODE = {'0 1 0 1': 'A',
        '0 1 1 1': 'B',
        '0 0 1 0': 'C',
        '1 1 0 1': 'D',
        '1 0 0 0': 'E',
        '1 1 0 0': 'F'
        }
result = ''
code_list = []
num = int(input())
for a in range(num):
    a = str(input())
    code_list.append(a)
for i in code_list:
    result += CODE[i]
print(result)
