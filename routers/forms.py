from fastapi import APIRouter
from ..pydantic.models import FormRequest
from ..database import SessionLocal
from fastapi import Depends
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/forms",
    tags=["forms"],
    responses={404: {"description": "No encontrado"}}
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/form")
async def form(form: FormRequest, db: Session = Depends(get_db)):
    """Save a form."""

    new_form = Form(name=form.name, address=form.address, phone=form.phone, items=form.items)
    db.add(new_form)
    db.commit()

    return {"message": "Form saved"}
