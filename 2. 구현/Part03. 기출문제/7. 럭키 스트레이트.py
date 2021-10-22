n = input()
n_len = len(n)
left_side = 0
right_side = 0

for i in n[:n_len//2]:
    left_side += int(i)
for i in n[n_len//2:]:
    right_side += int(i)

if left_side == right_side:
    print("LUCKY")
else:
    print('READY')
    