import sys

input = sys.stdin.readline

s = set()
m = int(input())

for _ in range(m):
    line = input().split()
    if not line:
        continue

    cmd = line[0]

    if cmd == 'all':
        s = set(range(1, 21))

    elif cmd == 'empty':
        s = set()

    else:
        num = int(line[1])

        if cmd == 'add':
            s.add(num)

        elif cmd == 'remove':
            s.discard(num)

        elif cmd == 'check':
            print(1 if num in s else 0)

        elif cmd == 'toggle':
            if num in s:
                s.remove(num)
            else:
                s.add(num)