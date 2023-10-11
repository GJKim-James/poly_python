from tkinter import *
from tkinter import messagebox


# 함수 선언 부분
def keyEvent(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키 " + chr(event.keycode))
    # event.keycode에는 눌려진 키의 숫자 값이 들어있음. chr() 함수로 문자 변환


# 메인 코드 부분
window = Tk()

window.bind("<Key>", keyEvent)  # <Key> 이벤트를 윈도우에서 사용

window.mainloop()
