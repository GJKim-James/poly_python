from tkinter import *
from tkinter import messagebox


# 함수 선언 부분
def clickLeft(event):  # 키보드나 마우스를 누르는 것을 이벤트(Event)라고 함
    messagebox.showinfo("마우스", "마우스 왼쪽 버튼이 클릭됨")


# 메인 코드 부분
window = Tk()

window.bind("<Button-1>", clickLeft)  # bind 함수는 위젯들의 이벤트와 실행할 함수 설정 가능, <Button-1>은 마우스 왼쪽 클릭을 의미

window.mainloop()  # mainloop() 함수는 이벤트(Event)가 발생하는 것을 기다리는 함수
