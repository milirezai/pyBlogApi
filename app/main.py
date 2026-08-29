from fastapi import FastAPI

app = FastAPI() 

@app.get("/")
def root():
    return "blog with fastApi"
