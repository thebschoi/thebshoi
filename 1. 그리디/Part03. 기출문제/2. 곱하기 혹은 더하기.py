s = str(input())
answer = 0

for idx, num in enumerate(s):
    if idx == 0:
        answer += int(num)
    else:
        if int(num) == 0 or int(s[idx-1]) == 0:
            answer += int(num)
        else:
            answer *= int(num)
print(answer)