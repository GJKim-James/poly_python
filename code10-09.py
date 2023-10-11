from tkinter import *
window = Tk()

button1 = Button(window, text="버튼1")
button2 = Button(window, text="버튼2")
button3 = Button(window, text="버튼3")

button1.pack(side=LEFT)  # 수평 정렬(왼쪽부터)
button2.pack(side=LEFT)  # 수평 정렬(왼쪽부터)
button3.pack(side=LEFT)  # 수평 정렬(왼쪽부터)

window.mainloop()
