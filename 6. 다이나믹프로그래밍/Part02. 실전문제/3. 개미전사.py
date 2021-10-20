# 식량창고 개수
n = int(input())
# 각 식량창고에 저장된 식량의 개수
k_list = list(map(int, input().split()))

d = [0] * 100
d[0] = k_list[0]
d[1] = max(k_list[0], k_list[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + k_list[i])
print(d[n-1])