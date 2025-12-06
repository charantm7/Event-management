from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"]
)


# instance / methods / route

names = [1, 2, 3, 4]
# 0, 1, 2, 3


@app.get("/")
def home():
    return names


@app.post("/hello/{name}")  # route
def hello(name: str):  # function

    names.append(name)
    print(names)

    return {"updated": names}


@app.delete("/items/{name}")
def deleted(name: int):

    names.remove(name)

    return (names)
