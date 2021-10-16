def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None 

n, target = map(int, input().split())
array = list(map(int, input().split()))

res = binary_search(array, target, 0, n-1)
if res == None:
    print('원소x')
else:
    print(res+1)