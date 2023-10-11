from tkinter import *
from tkinter.filedialog import *


# 함수 선언 부분
window = Tk()
window.geometry("400x100")

label1 = Label(window, text="선택된 파일 이름")
label1.pack()

saveFp = asksaveasfile(parent=window, mode="w", defaultextension=".jpg",
                       filetypes=(("JPG 파일", "*.jpg;*jpeg"), ("모든 파일", "*.*")))
# asksaveasfile()은 다른 이름으로 저장하는 함수
# defaultextension=".jpg"는 특별히 확장명을 지정하지 않으면 확장명을 jpg로 붙인다는 의미
label1.configure(text=saveFp)  # saveFp : <_io.TextIOWrapper name='C:/python/GIF/text.txt' mode='w' encoding='cp949'>
saveFp.close()

window.mainloop()
