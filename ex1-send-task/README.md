# Example 1. Send Task

## 개요
Celery 도커 컨테이너를 띄우고, 컨테이너 외부에서 task 요청을 보내는 예제입니다.

## 실행 방법
1. Celery 컨테이너를 띄웁니다.
```sh
docker-compose up
```
2. 가상환경 혹은 로컬 환경에 celery를 설치합니다.
```sh
pip3 install celery
```
3. send_task.py를 실행합니다.
```sh
python3 send_task.py
```
4. localhost:8888 에서 task가 잘 수행됨을 확인합니다. `./tmp/static/` 폴더에 `jpg`파일이 저장됨을 확인합니다.

## 참조
1. https://docs.celeryq.dev/en/stable/reference/celery.html#celery.Celery.send_task