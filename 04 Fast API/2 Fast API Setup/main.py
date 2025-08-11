from fastapi import FastAPI

# Create the FastAPI app
app = FastAPI()

# Define a root endpoint
@app.get("/")
def hello():
    return {"message": "Hello, World!"}

# 
@app.get("/about")
def about():
    return {"message": "This is the about page."}