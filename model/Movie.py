
from pydantic import BaseModel, Field
from typing import Optional


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_lenght=5, max_length=50)
    overview: str = Field(min_lenght=15, max_length=100)
    year: int = Field(le=2022)
    rating: float = Field(ge=0.1, le=9.9)
    category: str = Field(min_lenght=5, max_length=25)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "title": "Mi Pelicula",
                    "overview": "Descripcion de la pelicula",
                    "year": 2022,
                    "rating": 9.9,
                    "category": "Acción"
                }
            ]
        }
    }
