n, k = map(int, input().split())
answer = 0

while n != 1:
    if n % k == 0:
        n //= k
        answer += 1
    else:
        n -= 1
        answer += 1
print(answer)

# 다른 풀이
# import math
# n, k = map(int, input().split())
# answer = 0

# while (n % k != 0):
#     n -= 1
#     answer += 1
# answer += int(math.sqrt(k))
# print(answer)
