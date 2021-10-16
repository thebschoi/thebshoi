n, m = map(int, input().split())
n_list = list(map(int, input().split()))

# 이진탐색(반복문) 사용
start = 0
end = max(n_list)
result = 0
while(start <= end):
    total = 0
    mid = (start+end) // 2
    for n in n_list:
        if n > mid:
            total += n - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)    