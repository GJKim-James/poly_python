import sys

option = sys.argv[1]
print("Option : %s" % option)

if option == '-a':
    memo = sys.argv[2]
    print("Contents : %s" % memo)
    f = open("memo.txt", 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open("memo.txt", 'r')
    memo = f.read()
    f.close()
    print(memo)
