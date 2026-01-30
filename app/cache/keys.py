def user_key(user_id: int):
    return f"user:{user_id}"

def user_projects_key(user_id: int):
    return f"user:{user_id}:projects"

def project_tasks_key(project_id: int):
    return f"project:{project_id}:tasks"
