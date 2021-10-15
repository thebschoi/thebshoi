n = int(input())
input_list = [int(input()) for i in range(n)]
input_list.sort(reverse=True)

for i in input_list:
    print(i, end=' ')