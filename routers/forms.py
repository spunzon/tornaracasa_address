from fastapi import APIRouter
from ..pydantic.models import FormRequest
from ..database import engine
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import Annotated
router = APIRouter(
    prefix="/forms",
    tags=["forms"],
    responses={404: {"description": "No encontrado"}}
)

def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

@router.post("/form")
async def form(form: FormRequest, db: SessionDep):
    """Save a form."""

    new_form = Form(name=form.name, address=form.address, phone=form.phone, items=form.items)
    db.add(new_form)
    db.commit()

    return {"message": "Form saved"}
