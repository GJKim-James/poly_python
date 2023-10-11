from tkinter import *
from tkinter import messagebox

window = Tk()


# 함수 선언 부분
def myFunc():
    if chk.get() == 0:  # IntVar() 함수를 활용한 부분
        messagebox.showinfo("", "체크 버튼이 꺼졌어요.")
    else:  # 1
        messagebox.showinfo("", "체크 버튼이 켜졌어요.")


# 메인 코드 부분
chk = IntVar()  # IntVar() - 정수형 타입의 변수 생성
cb1 = Checkbutton(window, text="클릭하세요", variable=chk, command=myFunc)
ch2 = Checkbutton(window, text="O", variable=chk, activebackground="blue")

cb1.pack()
ch2.pack()

window.mainloop()
