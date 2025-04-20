from fastapi import FastAPI
import uvicorn

app = FastAPI()




@app.get("/messege/")
async def say_hello(message: str = "Hello, World!"):
    return dict(msg=message)


if __name__ == "__main__":
    uvicorn.run(app)
