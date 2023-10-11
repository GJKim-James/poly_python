from tkinter import *

window = Tk()

label1 = Label(window, text="CookBook~~Python을")
label2 = Label(window, text="열심히", font=("궁서체", 30), fg="blue")
label3 = Label(window, text="공부 중입니다.", bg="magenta", width=20, height=5, anchor=SE)

label1.pack()  # pack() 함수를 호출해야 window 화면에 표시됨
label2.pack()  # pack() 함수를 호출해야 window 화면에 표시됨
label3.pack()  # pack() 함수를 호출해야 window 화면에 표시됨

window.mainloop()
