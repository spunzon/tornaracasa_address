from pydantic import BaseModel
from typing import Optional, List, Dict

class FormRequest(BaseModel):
    name : str
    phone : str
    state : str
    email : str
    address : str
    items : List[str]
    document : str
