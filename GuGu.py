def GuGu(n):
    result = []  # 결과값을 리스트 형태로 출력

    i = 1
    while i < 10:
        result.append(n * i)
        i = i + 1
    return result


n = int(input("출력하고 싶은 단을 입력하세요 : "))
print(GuGu(n))
