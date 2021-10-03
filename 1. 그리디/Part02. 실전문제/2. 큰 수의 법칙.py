n, m, k = map(int, input().split())
data = list(map(int, input().split()))
answer = 0

data.sort(reverse=True)
# k+1을 한 묶음으로 봄
answer = (data[0] * k + data[1]) * (m//(k+1)) + data[0] * (m%(k+1))
print(answer)
