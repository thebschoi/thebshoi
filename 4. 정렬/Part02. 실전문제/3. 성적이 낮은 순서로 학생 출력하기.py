n = int(input())
s_info = [list(input().split()) for i in range(n)]
s_info.sort(key=(lambda data:int(data[1])))
for i in s_info:
    print(i[0], end=' ')