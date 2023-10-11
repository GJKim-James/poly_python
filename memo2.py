import sys

memo = input("메모장에 추가할 내용 : ")
f = open("memo.txt", 'a')
f.write(memo)
f.write("\n")
f.close()

f = open("memo.txt", 'r')
memo = f.read()
f.close()
print("메모장 내용 ↓ \n%s" % memo)
