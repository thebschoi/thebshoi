s = str(input())

res0 = 0
res1 = 0
for idx, i in enumerate(s):
    if i != '0':
        if idx == 0 or s[idx-1] != '1':
            res0 += 1
    elif i != '1':
        if idx == 0 or s[idx-1] != '0':
            res1 += 1
print(min([res0, res1]))