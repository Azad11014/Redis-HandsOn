from fastapi import FastAPI, HTTPException
from app.routes.routes import user_project_router

def create_app():
    app = FastAPI()


    @app.get("/")
    async def root():
        return {"message" : "root is up!"}
    app.include_router(user_project_router, prefix="" ,tags=["User & Projects"])
    return app
