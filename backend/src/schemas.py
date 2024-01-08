from pydantic import BaseModel, Field


class BasicSchema(BaseModel):
    id: str = Field(default="1234")
    type: str = Field(default="hello")
