from pydantic import BaseModel
from typing import Dict, Any

class WorldOntologyModel(BaseModel):
    ontology_path: str
    data: Dict[str, Any] = {}

    class Config:
        arbitrary_types_allowed = True