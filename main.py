from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello, World!"}

@app.get("/about")
def about():
    return {"message": "This is the about page."}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}