from fastapi import FastAPI

app_rm = FastAPI()


@app_rm.get("/")
def root():
    return {"message": "Agentic RM API is running"}