from celery import Celery
import os


app = Celery(__name__)

app.conf.update({
    'broker_url': os.environ.get('BROKER', 'amqp://rabbitmq:5672//'),
    'result_backend': os.environ.get('BACKEND', 'amqp://rabbitmq:5672//')
})
app.conf.beat_schedule = {
    'add-every-5-seconds': {
        'task': 'workers.tasks.add',
        'schedule': 5.0,
        'args': (16, 16)
    },
}


# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

#     # Calls test('world') every 30 seconds
#     sender.add_periodic_task(30.0, test.s('world'), expires=10)


# @app.task
# def test(arg):
#     print(arg)


# @app.task(bind=True, name='create_add', ignore_result=True)
# def add(x, y):
#     z = x + y
#     print(z)
