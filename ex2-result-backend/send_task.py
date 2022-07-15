from celery import Celery
import time

celery = Celery()
celery.conf.update({ 'broker_url': 'amqp://guest:guest@localhost:5672//', 'result_backend': 'rpc://' })
result = celery.send_task('task_wait')

while not result.ready():
    time.sleep(1)
    print('Waiting for result...')

print(f'Result: {result.get()}')