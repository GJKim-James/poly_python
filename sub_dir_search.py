import os


def search(dirname):
    try:
        filenames = os.listdir(dirname)  # os.listdir()은 지정 디렉터리 내의 모든 파일과 디렉터리를 리스트로 리턴
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):  # os.path.isdir(path)는 path가 디렉터리이면 True 반환
                search(full_filename)  # 재귀 호출
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass
    # try ~ except PermissionError를 사용한 이유는 os.listdir을 수행 했을 때 권한이 없는 디렉터리에 접근하더라도
    # 프로그램 오류로 종료되지 않고 계속 수행되도록 하기 위해서이다.


search("C:/")
