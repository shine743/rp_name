# 리눅스 기본 커멘드만 설치되있는 이미지
from python:3.9-alpine
# 컨테이너에서 실행할 명령어
run pip install --no-cache-dir flask
# 컨테이너에 배치할 파일
copy ./hello.py /hello.py
# 컨테이너 실행하고 실행될 명령어
cmd ["python3", "-m", "flask", "--app", "hello.py", "run", "--host=0.0.0.0"]
