n = int(input())
move_list = list(map(str, input().split()))

x_pos = 1
y_pos = 1

for i in move_list:
    if i == 'R' and y_pos < n:
        y_pos += 1
    elif i == 'L'and y_pos > 1:
        y_pos -= 1
    elif i == 'U' and x_pos > 1:
        x_pos -= 1
    elif i == 'D' and x_pos < n:
        x_pos += 1
print(x_pos, y_pos)
