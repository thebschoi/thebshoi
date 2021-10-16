# 이진탐색(재귀함수) 사용
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


for m in m_list:
    res = binary_search(n_list, m, 0, n-1)
    if res == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')

# 다른 풀이
# 집합(set()) 사용
# n = int(input())
# n_list = set(map(int, input().split()))
# m = int(input())
# m_list = list(map(int, input().split()))

# for m in m_list:
#     if m in n_list:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')