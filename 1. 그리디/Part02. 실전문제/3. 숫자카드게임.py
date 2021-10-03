n, m = map(int, input().split())
min_list = []

for i in range(n):
    num_list = list(map(int, input().split()))
    min_list.append(min(num_list))
answer = max(min_list)
print(answer)
