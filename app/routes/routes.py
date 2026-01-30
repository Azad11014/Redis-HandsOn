from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.database_connection import get_db

from app.services.user_service import UserServices

usr_ops = UserServices()

user_project_router = APIRouter()


@user_project_router.post("/user")
async def create_user(
    name : str,
    db : AsyncSession = Depends(get_db)
):
    try:
        return await usr_ops.create_user(name, db)

    except Exception as e:
        raise

@user_project_router.get("/user")
async def get_users(
    user_id : int,
    db : AsyncSession = Depends(get_db)
):
    try:
        return await usr_ops.get_user(user_id, db)
    except Exception as e:
        raise


@user_project_router.get("/projects")
async def get_projects(
    user_id : int,
    db : AsyncSession = Depends(get_db)
):
    try:
        return await usr_ops.get_user_projects(user_id, db)
    except Exception as e:
        raise