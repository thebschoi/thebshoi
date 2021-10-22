# readline()으로 입력받기 : input()보다 속도 빠름
import sys
n = int(sys.stdin.readline().rstrip())

# 여러개 입력받기
n, m = map(int, input().split())

# 한 칸씩 띄워 입력 받아서 list에 저장
data = list(map(int, input().split()))


# sort()
# 원본 데이터가 바뀌는 정렬
data = [3,5,1,4,2]
# 오름차순
data.sort() # data = [1,2,3,4,5]
# 내림차순
data.sort(reverse=True) # data = [5,4,3,2,1]
# sort()에서 print
print(data.sort()) # none 이 나온다.

# sorted() : 원본 데이터는 그대로 두고 새로 정렬
data = [3,5,1,4,2]
# 오름차순
sorted_data = sorted(data) # sorted_data = [1,2,3,4,5]
# 내림차순
sorted_data = sorted(data, reverse=True) # sorted_data = [5,4,3,2,1]

# min, max
data = [3,5,1,4,2]
min(data) # 1
max(data) # 5

# 제곱근
import math
math.sqrt() # math.sqrt(2) = 1.414...

# 아스키코드
ord('a') # 97

# 위치 찾기
a = '123456'
a.index('1') # 0

# 스와프 : 리스트 내 두 원소의 위치 변경
array = [3,5]
array[0], array[1] = array[1], array[0]
print(array) # [5,3]

# 알파벳 정렬하기(오름차순)
s = '1bc2aa3s4'
new_s = ''.join(sorted(list(s))) # new_s : 1234aabcs
