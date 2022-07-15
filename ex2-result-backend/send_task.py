from celery import Celery
import time

def progress_bar(current, total):
    bar = ''
    for i in range(total):
        if i <= current:
            bar += '⬛'
        else:
            bar += '⬜'
    return bar

celery = Celery()
celery.conf.update({ 'broker_url': 'amqp://guest:guest@localhost:5672//', 'result_backend': 'rpc://' })
result = celery.send_task('task_wait')
print(f'Status: {result.status}')

print(f'Result: {result.get()}')

while not result.ready():
    time.sleep(1)
    print(f'Waiting for result... Status: {result.status}')
    if result.status == 'PROGRESS':
        print(progress_bar(result.info['current'], result.info['total']))

print(f'Result: {result.get()}')