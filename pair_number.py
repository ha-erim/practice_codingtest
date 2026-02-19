# 프로그래머스 - 숫자 짝꿍
def solution(X, Y):
    pair = []
    X = list(X)
    new_Y = list(Y)

    for x in X:
        if x in new_Y:               # 존재 여부부터 확인
            idx = new_Y.index(x)     # 그 다음 index 사용
            new_Y.pop(idx)           # 해당 원소 1개 제거
            pair.append(x)           # 문자 그대로 저장

    if pair:
        pair.sort(reverse=True)      # 문자 정렬(내림차순)
        result = ''.join(pair)

        # 프로그래머스 "숫자 짝꿍" 기준 처리(전체가 0이면 "0")
        if result[0] == '0':
            return "0"
        return result

    return "-1"

result = solution("5525","1255")

print(result)