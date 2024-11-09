from openai import OpenAI
import base64
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def encode_image(image_path):
    """Codifica la imagen en base64"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def extraer_datos_factura(image_path):
    """Extrae el nombre del titular y domicilio de una factura de agua"""

    # Inicializar el cliente de OpenAI
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    # Codificar la imagen
    base64_image = encode_image(image_path)

    # Preparar el prompt para GPT-4 Vision
    prompt = """Por favor extrae la siguiente información de esta factura:
    1. Nombre completo del titular
    2. Domicilio completo
    Presenta la información en formato JSON."""

    # Realizar la solicitud a la API
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        max_tokens=300
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    # Ruta de la imagen de la factura
    imagen_factura = "screenshot_factura.png"

    try:
        resultado = extraer_datos_factura(imagen_factura)
        print("Información extraída:")
        print(resultado)
    except Exception as e:
        print(f"Error al procesar la factura: {str(e)}")
