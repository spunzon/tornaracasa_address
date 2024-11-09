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

@router.post("/form")
async def form(form: FormRequest, db: SessionDep):
    """Save a form."""

    # Verificar si el usuario ya existe por teléfono
    existing_user = db.query(User).filter(User.phone == form.phone).first()

    if existing_user:
        # Verificar items ya pedidos
        existing_orders = db.query(Order).filter(Order.user_id == existing_user.id).all()
        existing_item_ids = {order.item_id for order in existing_orders}

        # Verificar si algún item solicitado ya fue pedido
        duplicate_items = set(form.items) & existing_item_ids
        if duplicate_items:
            raise HTTPException(
                status_code=400,
                detail=f"Ya has pedido los siguientes items: {duplicate_items}"
            )

    # Crear nuevo usuario si no existe
    if not existing_user:
        user = User(
            name=form.name,
            address=form.address,
            phone=form.phone
        )
        db.add(user)
        db.flush()  # Para obtener el ID del usuario
    else:
        user = existing_user

    # Crear órdenes para cada item
    for item_id in form.items:
        new_order = Order(
            user_id=user.id,
            item_id=item_id,
            quantity=1  # Puedes modificar esto si necesitas manejar cantidades
        )
        db.add(new_order)

    db.commit()

    return {"message": "Pedido guardado exitosamente"}
