from pydantic import BaseModel
from typing import Optional, List, Dict

class FormRequest(BaseModel):
    name : str
    address : str
    phone : str
    items : List[int]
