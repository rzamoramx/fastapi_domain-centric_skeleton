# Application entry point
from fastapi import FastAPI
from app.api.routes import users, items
from app.core.config import settings
from app.db.database import Base, engine

app = FastAPI(title=settings.PROJECT_NAME)

# Init database
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(items.router, prefix="/items", tags=["items"])


@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI application"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
