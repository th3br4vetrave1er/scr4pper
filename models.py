from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

# creating base model 'News'


class News(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    link: str
    published_at: datetime
    description: Optional[str] = None
