from fastapi import FastAPI

from app.api.v1.users import router as users_router


app = FastAPI(
    title="MACHINASENSE API",
    version="0.1.0",
    description="AI-powered Manufacturing Intelligence Platform",
)


app.include_router(
    users_router,
    prefix="/api/v1",
)


@app.get("/")
def health_check():
    return {
        "name": "MACHINASENSE",
        "version": "0.1.0",
        "status": "healthy",
    }