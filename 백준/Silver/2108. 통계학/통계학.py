import sys

input = sys.stdin.readline
n = int(input())
nums = []

# 카운팅 배열 생성 (-4000부터 4000까지 8001개)
freq = [0] * 8001
sum_val = 0

for _ in range(n):
    num = int(input())
    nums.append(num)
    sum_val += num
    # 입력값을 인덱스로 변환 (예: -4000 -> 0, 4000 -> 8000)
    freq[num + 4000] += 1

# 1. 평균
print(int(round(sum_val / n)))

# 2. 중앙값
nums.sort()
print(nums[n // 2])

# 3. 최빈값 (카운팅 배열 기반)
max_freq = max(freq)
modes = []
for i in range(8001):
    if freq[i] == max_freq:
        modes.append(i - 4000) # 다시 원래 숫자로 변환

modes.sort() # 빈도수가 같은 녀석들 정렬

if len(modes) > 1:
    print(modes[1]) # 2번째로 작은 값
else:
    print(modes[0])

# 4. 범위
print(max(nums) - min(nums))