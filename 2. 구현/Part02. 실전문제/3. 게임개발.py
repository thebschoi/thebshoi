n, m = map(int, input().split())
x, y, d = map(int, input().split())

game_map = []

for i in range(n):
    row = list(map(int, input().split()))
    game_map.append(row)

