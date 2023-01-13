s = """502
503
504
503, 504
505
503
503, 504
505
504, 505
506
602
603
602, 603
604
603, 604
504, 603
505, 603
504, 602, 604
506, 603
504, 505, 604
1002
1003
1002, 1003
1004
1003, 1004
506, 603, 1003
505, 603, 1004
604, 1002, 1004
605
505, 605, 1004
506, 604, 1004
505, 506, 1003
505, 604, 1004
505, 1005
606
505, 605, 1004
505, 1005
505, 605, 1004
506, 1005
1006
505, 606, 1005
505, 605, 1005
605, 606, 1005
1005, 1006
506, 606, 1006"""

dif = """1
1
3
5
5
1
1
1
2
3
1
1
2
3
5
1
2
2
3
3
1
1
2
3
5
2
2
2
1
4
3
2
2
2
3
3
2
3
3
3
3
2
3
2
5"""
dif = list(map(int, dif.split("\n")))
n_levels = 5
s = s.split("\n")
orders = []
for i in range(len(s)):
    orders.append(s[i].split(", "))
res = []
for i in range(0, len(orders), 5):
    res.append(orders[i:i+5])

res = res[0:len(res)]
t = res.copy()
m = 0
for i in range(len(res)):
    for j in range(len(res[i])):
        for k in range(len(res[i][j])):
                res[i][j][k]=  int(res[i][j][k].split(",")[0])
        t[i][j] = [dif[m], res[i][j]]
        m += 1

print(res)