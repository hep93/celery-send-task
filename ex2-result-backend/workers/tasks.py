from workers.config import app
from func.thumbnail import create_thumbnail
import time

@app.task(bind=True, name='task_wait', track_started=True)
def wait(self):
    for i in range(10):
        print(f'Waiting.... {i} sec')
        time.sleep(1)
        self.update_state(state='PROGRESS', meta={'current': i, 'total': 10})
    return 'This is a result!'