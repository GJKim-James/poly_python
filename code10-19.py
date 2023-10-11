from tkinter import *
from tkinter.simpledialog import *  # 입력창 사용하기 위해 tkinter.simpledialog 모듈 임포트

# 함수 선언 부분
window = Tk()
window.geometry("400x100")

label1 = Label(window, text="입력된 값")
label1.pack(expand=1)

value = askinteger("확대배수", "주사위 숫자(1~6)를 입력하세요", minvalue=1, maxvalue=6)
# askinteger("제목", "내용", 옵션), askfloat() - 실수, askstring() - 문자열

label1.configure(text=str(value))  # 입력받은 숫자를 문자열로 반환
window.mainloop()
