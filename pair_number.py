# 프로그래머스 - 숫자 짝꿍

# 내가 구현한 버전
# 이 방식은 in + index 때문에 최악 O(n^2)이라 입력이 크면 느릴 수 있음
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
        if result[0] == '0':
            return "0"
        return result
    return "-1"

# GPT가 만들어준 버전
# 속도 빠르고, counting 하는 버전
def solution(X, Y):
    count_x = [0] * 10
    count_y = [0] * 10

    # 각 숫자 개수 세기
    for ch in X:
        count_x[int(ch)] += 1
    for ch in Y:
        count_y[int(ch)] += 1

    result = []

    # 큰 숫자부터 만들기
    for i in range(9, -1, -1):
        common = min(count_x[i], count_y[i])
        if common > 0:
            result.append(str(i) * common)

    if not result:
        return "-1"

    answer = ''.join(result)

    # 전부 0이면 "0"
    if answer[0] == '0':
        return "0"

    return answer


result = solution("5525","1255")

print(result)