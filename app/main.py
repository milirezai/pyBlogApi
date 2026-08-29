from fastapi import FastAPI

app = FastAPI() 

@app.get("/")
def root():
    return "hello fast api"

@app.get("/mili")
def mili():
    return 'mili in fast api'

@app.get('/post')
def post():
    return 'hi post'
