import os


def search(dirname):
    filenames = os.listdir(dirname)  # os.listdir()은 지정 디렉터리 내의 모든 파일과 디렉터리를 리스트로 리턴
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        if os.path.isdir(full_filename):  # os.path.isdir(path)는 path가 디렉터리이면 True 반환
            print("디렉터리? : ", os.path.isdir(full_filename))
            search(full_filename)  # 재귀 호출
        else:
            ext = os.path.splitext(full_filename)[-1]
            if ext == '.py':
                print(full_filename)


search("C:/")
