def solution(myString):
    string = myString.lower()
    result = string
    if 'a' in string:
        result = string.replace('a','A')
    return result