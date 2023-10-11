from tkinter import *
window = Tk()

btnList = [None] * 3

for i in range(0, 3):
    btnList[i] = Button(window, text="버튼" + str(i + 1))

for btn in btnList:
    # btn.pack(side=RIGHT)  # 수평 정렬(오른쪽부터)

    # btn.pack(side=TOP)  # 수직 정렬(위에서부터)
    # btn.pack(side=BOTTOM)  # 수직 정렬(아래에서부터)

    # btn.pack(side=TOP, fill=X)  # 폭 조정, fill=X는 윈도우 창 폭에 맞춤

    # btn.pack(side=TOP, fill=X, padx=10, pady=10)  # 위젯 간의 여백 주기

    # btn.pack(side=TOP, fill=X, ipadx=10, ipady=10)  # 위젯 내부 여백 주기

    btn.pack(side=TOP, fill=X, ipadx=10, ipady=10, padx=10, pady=10)  # 위젯 내부, 외부 여백 주기

window.mainloop()
