
from pydantic import BaseModel, Field
from typing import Optional


class Category(BaseModel):
    id: Optional[int] = None
    category: str = Field(min_lenght=5, max_length=25)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "category": "Acción"
                }
            ]
        }
    }
