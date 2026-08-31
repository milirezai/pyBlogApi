from main import app

@app.get('/posts')
async def all():
    return 'all posts'