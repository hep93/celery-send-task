from celery import Celery
import os


app = Celery(__name__)

app.conf.update({
    'broker_url': os.environ.get('BROKER', 'amqp://rabbitmq:5673//'),
    'result_backend': os.environ.get('BACKEND', 'amqp://rabbitmq:5673//')
})
app.conf.beat_schedule = {
    'add-every-10-seconds': {
        'task': 'workers.tasks.add',
        'schedule': 10.0,
        'args': (16, 16)
    },
}
