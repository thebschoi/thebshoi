p = str(input())
x = ord(p[0]) - ord('a') + 1
y = int(p[1])

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

answer = 0
for step in steps:
    next_x = x + step[0]
    next_y = y + step[1]
    if next_x > 0 and next_x < 9 and next_y > 0 and next_y < 9:
        answer += 1
print(answer)

# p = str(input())
# x = p[0]
# y = int(p[1])

# x_list = ['a','b','c','d','e','f','g','h']
# x = x_list.index(x) + 1

# answer = 0

# if (x + 2) < 9:
#     if (y + 1) < 9:
#         answer += 1
#     if (y - 1) > 0:
#         answer += 1
# if (x - 2) > 0:
#     if (y + 1) < 9:
#         answer += 1
#     if (y - 1) > 0:
#         answer += 1
# if (y + 2) < 9:
#     if (x + 1) < 9:
#         answer +=1
#     if (x - 1) > 0:
#         answer += 1
# if (y - 2) > 0:
#     if (x + 1) < 9:
#         answer +=1
#     if (x - 1) > 0:
#         answer += 1
# print(answer)