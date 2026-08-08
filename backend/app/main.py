from fastapi import FastAPI

app = FastAPI(
    title="MACHINASENSE API",
    version="0.1.0",
    description="AI-powered Manufacturing Intelligence Platform",
)


@app.get("/")
def health_check():
    return {
        "name": "MACHINASENSE",
        "version": "0.1.0",
        "status": "healthy",
    }