array = [('바나나', 2), ('사과', 5), ('당근', 3)]

# key 값으로는 하나의 함수가 들어가야 한다.
def setting(data):
    return data[1]

ans = sorted(array, key = setting)
print(ans)

# 람다를 사용한 방식
# res = sorted(array, key = (lambda data: data[1]))
# print(res)