n = int(input())

people = []
res = []

for _ in range(n):
    x, y = map(int, input().split())
    people.append((x, y))

for i in range(n):
    count = 1
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            count += 1
    
    res.append(str(count))

print(" ".join(res))
