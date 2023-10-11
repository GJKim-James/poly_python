from tkinter import *
from tkinter.filedialog import *

# 함수 선언 부분
window = Tk()
window.geometry("400x100")

label1 = Label(window, text="선택된 파일 이름")
label1.pack()

filename = askopenfilename(parent=window, filetypes=(("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
# askopenfilename() 함수는 경로를 포함해서 선택한 파일명을 반환
# filetypes는 값으로 튜플을 받음. 그리고 각 튜플 안에서 다시 튜플로 ("표시할 글자", "확장명") 형식을 구성함

label1.configure(text=str(filename))  # filename 출력, 원래 타입 'str' 이라서 안써도 무관

window.mainloop()
