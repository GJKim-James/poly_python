marks = [90, 25, 67, 45, 80]

number = 0

for point in marks:
    number = number + 1
    if point >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)
