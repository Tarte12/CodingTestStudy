import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = []

for _ in range(n):
    lst.append(input().strip())

cnt = 64

for i in range(n-7):
    for j in range(m-7):
        w_start_count = 0 # (0, 0)이 W인 경우 색칠할 개수
        b_start_count = 0 # (0, 0)이 B인 경우 색칠할 개수

        for x in range(i, i+8):
            for y in range(j, j+8):
                # x+y 합이 짝수인 칸은 시작점과 같은 색
                # x+y 합이 홀수인 칸은 시작점과 다른 색
                if (x+y) % 2 == 0:
                    if lst[x][y] != 'W':
                        w_start_count += 1
                    if lst[x][y] != 'B':
                        b_start_count += 1
                else:
                    if lst[x][y] != 'B':
                        w_start_count += 1
                    if lst[x][y] != 'W':
                        b_start_count += 1

        cnt = min(cnt, w_start_count, b_start_count)

print(cnt)