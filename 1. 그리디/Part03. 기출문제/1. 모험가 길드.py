n = int(input())
h_list = list(map(int, input().split()))
h_list.sort(reverse=True)
answer = 0

s_idx = 0
p_idx = 0
for i in range(len(h_list)):
    num_of_member = h_list[s_idx]
    if i == p_idx+num_of_member-1:
        answer += 1
        s_idx = h_list[i]
        p_idx = i+1
print(answer)


