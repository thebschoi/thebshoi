s = input()
new_s = ''.join(sorted(list(s)))
sum_of_num = 0
answer = ''
for i in new_s:
    if i.isdigit():
        sum_of_num += int(i)
    else:
        answer += i
print(answer+str(sum_of_num))