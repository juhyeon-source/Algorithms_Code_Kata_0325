def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        a = parts[i]
        answer += my_strings[i][a[0]:a[1]+1]
    return answer