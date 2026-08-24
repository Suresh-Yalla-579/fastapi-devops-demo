from fastapi import FastAPI

app = FastAPI(
    title="FastAPI DevOps Demo",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "FastAPI DevOps Demo",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/hello/{name}")
def hello(name: str):
    return {
        "message": f"Hello {name}!"
    }