from fastapi import APIRouter, HTTPException, Depends, Request
import os
from sqlalchemy.orm import Session
from ..database import SessionLocal, engine, User, Base, InvitationCode
from fastapi.responses import RedirectResponse, Response
from shapely.geometry import Point, Polygon

router = APIRouter(
    prefix="/validation",
    tags=["validation"],
    responses={404: {"description": "No encontrado"}}
)

@router.get("/validate_address")
async def validate_address(address: str):
    """Validate an address."""
    return {"message": "Address validated"}

@router.get("/validate_coordinates")
async def validate_coordinates(latitude: float, longitude: float):
    """
    Valida que las coordenadas proporcionadas estén dentro de un polígono determinado.
    """
    try:
        # Definir el polígono complejo (por ejemplo, un polígono con múltiples vertices)
        polygon_coordinates = [
            (-30.0, 10.0),
            (-25.0, 15.0),
            (-20.0, 10.0),
            (-25.0, 5.0),
            (-30.0, 10.0)
        ]
        polygon = Polygon(polygon_coordinates)

        # Crear un punto a partir de las coordenadas proporcionadas
        point = Point(longitude, latitude)

        if polygon.contains(point):
            return {"message": "ok"}
        else:
            return {"message": "ko"}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al validar las coordenadas: {str(e)}"
        )
