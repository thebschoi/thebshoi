d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 문제
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))