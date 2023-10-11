import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " ")
print("tab을 space로 바꾼 결과 ↓\n", space_content)

f = open(dst, 'w')
f.write(space_content)
f.close()
