n = int(input())
h_list = list(map(int, input().split()))
h_list.sort(reverse=True)
answer = 0

for idx, h in enumerate(h_list):
    if p_num-1 == idx:
        answer + 1
        p_num = h_list[idx+1]

