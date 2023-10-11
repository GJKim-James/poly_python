from tkinter import *

window = Tk()

mainMenu = Menu(window)  # 윈도우 창에서 메뉴 기능을 사용 가능
window.config(menu=mainMenu)  # 윈도우 창에 '파일' 메뉴 등록

fileMenu = Menu(mainMenu)  # mainMenu에 fileMenu(열기, 종료) 추가
mainMenu.add_cascade(label="파일", menu=fileMenu)  # '파일'을 누르면 다른 메뉴가 확장되어야 하므로 add_cascade() 함수 사용
fileMenu.add_command(label="열기")  # '열기'를 누르면 어떤 작동을 해야하기 때문에 add_command() 함수 사용
fileMenu.add_separator()  # 메뉴 사이에 구분선 넣는 함수
fileMenu.add_command(label="종료")  # '종료'를 누르면 어떤 작동을 해야하기 때문에 add_command() 함수 사용

window.mainloop()
