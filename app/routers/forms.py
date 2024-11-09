from fastapi import APIRouter, HTTPException
from ..pydantic_models import FormRequest
from ..database import engine, User, Item, Order
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

@router.post("/order")
async def order(form: FormRequest, db: SessionDep):
    """Save a form."""

    # Verificar si el usuario ya existe por teléfono
    existing_user = db.query(User).filter(User.email == form.email).first()

    if existing_user:
        return {"message": "Usuario ya existe"}

    # Crear nuevo usuario si no existe
    if not existing_user:
        user = User(
            name=form.name,
            address=form.address,
            phone=form.phone,
            email=form.email,
            state=form.state,
            document=form.document
        )
        db.add(user)
        db.flush()  # Para obtener el ID del usuario


    # Crear órdenes para cada item
    for item in form.items:
        new_order = Order(
            user_id=user.id,
            item_id=item,
        )
        db.add(new_order)

    db.commit()

    return {"message": "Pedido guardado exitosamente"}
