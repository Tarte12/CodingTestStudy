import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nolisten = set()
nolook = set()
ans =  []

for _ in range(n):
    nolisten.add(input().strip())

for _ in range(m):
    nolook.add(input().strip())

ans = sorted(list(nolisten & nolook))

print(len(ans))
for person in ans:
    print(person)