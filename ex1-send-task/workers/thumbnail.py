from workers.config import app
from func.thumbnail import create_thumbnail

@app.task(bind=True, name='create_thumbnail')
def create(self, url, filename):
    create_thumbnail(url, filename)