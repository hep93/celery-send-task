# Example 2. Result Backend

## 개요
Celery에서 result backend에 결과를 저장하는 방법, 그리고 저장된 결과를 가져오는 방법에 대한 예시입니다. 추가로 task에 대한 status를 저장하고, custom status를 이용해 progress bar를 출력합니다.

## 설명
- Task를 호출하게 되면 result 인스턴스가 반환됩니다. 그 result 인스턴스에서 해당 task에 대한 상태를 불러올 수 있습니다.
```py
result.ready() # task가 완료 되었는지 확인합니다
```
- `result.get()`을 호출하면 결과 값을 가져올 수 있습니다. 만약 task가 완료되지 않았다면, 완료 될 때까지 기다리게 됩니다. `timeout` 옵션으로 `result.get(timeout=10)`과 같이 기다리는 시간을 설정할 수 있습니다. 하지만 동기 실행이 되므로 대부분의 경우 완료를 기다리는 것은 바람직하지 않습니다.
- Task 함수 안에서 `bind=True` 옵션을 넣게 되면 self 인자로부터 task instance를 참조할 수 있게 됩니다. `self.update_state` 함수를 사용해 task의 상태를 설정할 수 있습니다.
```py
@app.task(bind=True, name='task_wait', track_started=True)
def wait(self):
    for i in range(10):
        print(f'Waiting.... {i} sec')
        time.sleep(1)
        self.update_state(state='PROGRESS', meta={'current': i, 'total': 10})
    return 'This is a result!'
```
- Task의 상태를 읽어서 progress bar를 만들 수 있습니다.
```py
if result.status == 'PROGRESS':
    print(progress_bar(result.info['current'], result.info['total']))
```




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
4. 터미널에 출력되는 결과를 확인합니다.
```sh
Status: PENDING
Waiting for result... Status: PROGRESS
⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
Waiting for result... Status: PROGRESS
⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
Waiting for result... Status: PROGRESS
⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
Waiting for result... Status: PROGRESS
⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜
Waiting for result... Status: PROGRESS
⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜
Waiting for result... Status: PROGRESS
⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜
Waiting for result... Status: PROGRESS
⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜
Waiting for result... Status: PROGRESS
⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜
Waiting for result... Status: PROGRESS
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜
Waiting for result... Status: SUCCESS
Result: This is a result!
````

## 참조
1. https://docs.celeryq.dev/en/stable/userguide/tasks.html#result-backends