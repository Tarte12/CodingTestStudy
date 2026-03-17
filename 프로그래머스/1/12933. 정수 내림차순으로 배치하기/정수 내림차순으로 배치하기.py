def solution(n):
    answer = ''
    lst = sorted(list(str(n)), reverse=True)
    answer = "".join(lst)
    return int(answer)