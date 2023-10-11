result = 0

for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        result += n

print("1000 미만의 자연수 중 3과 5의 배수 합 : %d" % result)
