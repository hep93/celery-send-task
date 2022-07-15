from celery import Celery

celery = Celery()
celery.conf.update({ 'broker_url': 'amqp://guest:guest@localhost:5672//', 'result_backend': 'rpc://' })
celery.send_task('create_thumbnail', ('https://tinyjpg.com/images/social/website.jpg', 'abc.jpg'))