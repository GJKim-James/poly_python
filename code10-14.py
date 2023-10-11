from tkinter import *
from tkinter import messagebox


# 함수 선언 부분
def clickImage(event):
    messagebox.showinfo("마우스", "토끼에서 마우스가 클릭됨")


# 메인 코드 부분
window = Tk()
window.geometry("400x400")

photo = PhotoImage(file="gif/rabbit.gif")
label1 = Label(window, image=photo)

label1.bind("<Button>", clickImage)  # window.bind()가 아니라 label1.bind()이기 때문에 이미지를 클릭했을 때만 작동
# <Button> 이기 때문에 마우스 어떤 클릭을 해도 작동

label1.pack(expand=1, anchor=CENTER)  # expand는 미사용 공간 확보 여부(Boolean)
window.mainloop()
