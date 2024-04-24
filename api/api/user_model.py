from pydantic import BaseModel
from typing import Union, Optional


class UserModel(BaseModel):
    id: Union[str, int]
    first_name: str
    last_name: str
    description: Optional[str] = None

