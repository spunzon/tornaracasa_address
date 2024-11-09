from fastapi import APIRouter, HTTPException, Depends, Request
from shapely.geometry import Point, Polygon

router = APIRouter(
    prefix="/address",
    tags=["address"],
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
        polygon_coordinates = [
            (-1.026571949077777, 39.76963362870961),
            (-1.3282066449683612, 39.58013404975304),
            (-1.3178943476732456, 39.45085808826383),
            (-0.7803658511488436, 39.35523839320243),
            (-0.4207244829722754, 39.40505667594394),
            (-0.391076628247248, 39.43592615293662),
            (-0.4336148545905303, 39.4876765062659),
            (-0.545761087679125, 39.6923091706428),
            (-0.7507179964250383, 39.786474882295096),
            (-1.0291500234009447, 39.77161516655957)]

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
