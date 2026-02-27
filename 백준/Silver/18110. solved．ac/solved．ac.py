import sys
input = sys.stdin.readline

n = int(input()) # 난이도 의견 갯수

if n == 0:
    print(0)
    sys.exit()

lst = []

for i in range(n):
    lst.append(int(input())) # 사용자들이 제출한 난이도 의견 n개 삽입

lst.sort() #오름차순 정렬

cut = int((n*0.15)+0.5)

avg = sum(lst[cut:n-cut])/ (n-2*cut)

print(int(avg + 0.5))