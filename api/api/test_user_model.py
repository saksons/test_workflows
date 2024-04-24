from pydantic import BaseModel
from typing import Union, Optional


class TestUserModel(BaseModel):
    id: Union[str, int]
    first_name: str
    last_name: str
    description: Optional[str] = None

