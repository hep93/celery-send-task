from workers.config import app


@app.task(bind=True, name='create_add', ignore_result=True)
def add(x, y):
    z = x + y
    print(z)
