n, m = map(int, input().split())
accounts = [int(input()) for _ in range(n)]

min_possible = 0
max_possible = max(accounts)
while max_possible - min_possible > 1:
    curent = (min_possible + max_possible) // 2
    if sum([accounts[i] // curent for i in range(n)]) < m:
        max_possible = curent
    else:
        min_possible = curent

print(min_possible)