from tkinter import *
from tkinter import messagebox

# 전역 변수 선언 부분
btnList = [None] * 9
fnameList = ["froyo.gif", "gingerbread.gif", "honeycomb.gif", "icecream.gif",
             "jellybean.gif", "kitkat.gif", "lollipop.gif", "marshmallow.gif", "nougat.gif"]
photoList = [None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

# 메인 코드 부분
window = Tk()
window.geometry("210x210")

for i in range(0, 9):
    photoList[i] = PhotoImage(file="gif/" + fnameList[i])
    btnList[i] = Button(window, image=photoList[i])

for i in range(0, 3):
    for k in range(0, 3):  # 3 x 3 모양의 이미지 배열
        btnList[num].place(x=xPos, y=yPos)  # 위젯을 고정 위치에 배치하기 위해 pack() 대신 place() 함수 사용
        num += 1
        xPos += 70
    xPos = 0  # 2번째 줄부터 다시 이미지 넣기 시작
    yPos += 70

window.mainloop()
