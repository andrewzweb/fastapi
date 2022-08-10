from pydantic import BaseModel
import datetime


class Job(BaseModel):
    id: int
    user_id: int
    title: str
    description: str
    salary_from: int
    salary_to: int
    is_active: bool = True
    updated_at: datetime.datetime
    created_at: datetime.datetime

class JobIn(BaseModel):
    title: str
    description: str
    salary_from: int
    salary_to: int
    is_active: bool = True
