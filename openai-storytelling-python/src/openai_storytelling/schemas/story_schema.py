from pydantic import BaseModel

class StorySchema(BaseModel):
    title: str
    content: str
    author: str

    class Config:
        orm_mode = True