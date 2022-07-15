from workers.config import app
from func.thumbnail import create_thumbnail
import time

@app.task(bind=True, name='task_wait')
def wait(self):
    for i in range(10):
        print(f'Waiting.... {i} sec')
        time.sleep(1)
    return 'This is a result!'