from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database.database_connection import get_db
from app.models.models import User, Project, Task

from app.cache.keys import user_key, user_projects_key, project_tasks_key
from app.cache.helpers import set_cache, get_cache, delete_cache


class UserServices:

    async def create_user(self, name : str, db : AsyncSession):
        try:
            user = User(name = name)

            db.add(user)
            await db.commit()
            await db.refresh(user)

            return {"id": user.id, "name": user.name}

        except Exception as e:
            await db.rollback()
            raise HTTPException(status_code=500, detail=f"Something went wrong : {str(e)}")
        
    async def get_user(self, user_id : int, db : AsyncSession):
        try:
            #get the key
            key = user_key(user_id)
            #check is cache exists with taht key
            cached_data = get_cache(key)
            if cached_data:
                return {"source": "cache", "data": cached_data}
            
            #if not cached then query the db
            result = await db.execute(select(User).where(User.id==user_id))
            user = result.scalar_one_or_none()
            if not user:
                return None
            data = {"id": user.id, "name": user.name}
            #set cache for the retieved data
            try:
                print(f"Value chached : {key}")
                set_cache(key=key, value=data, ttl=120)
            except Exception as e:
                print(str(e))

            return {"source": "db", "data": data}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Something went wrong : {str(e)}")
        

    async def get_user_projects(self, user_id : int ,db : AsyncSession):
        try:
            key = user_projects_key(user_id)

            cached_data = get_cache(key)
            if cached_data:
                return {"source": "cache", "data": cached_data}
            #make db query
            result = await db.execute(select(Project).where(Project.user_id == user_id))
            projects = [{"id": p.id, "name": p.name} for p in result.scalars()]

            try:
                print(f"Value chached : {key}")
                set_cache(key=key, value=projects, ttl=120)
            except Exception as e:
                print(str(e))
            

            return {"source": "db", "data": projects}
        except Exception as e:
            raise HTTPException(status_code=500 ,detail=f"Something went wrong : {str(e)}")