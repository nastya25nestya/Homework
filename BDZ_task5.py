# пятая задача
n, m = map(int, input().split())
accounts = [int(input()) for _ in range(n)]
max_possible = (sum(accounts) // m)
summ_found = False
while not summ_found and max_possible > 0:
    cnt = 0
    accounts_tmp = accounts.copy()
    i = 0
    while i < len(accounts_tmp) and cnt < m:
        if accounts_tmp[i] >= max_possible:
            accounts_tmp[i] -= max_possible
            cnt += 1
        else:
            accounts_tmp.pop(i)
    if cnt == m:
        summ_found = True
    else:
        max_possible -= 1
if max_possible:
    print(max_possible)
else:
    print(0)