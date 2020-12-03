from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from .price import Price


@dataclass
class Shampoo:
    name: str
    brand: str
    brand_line: str
    price: List[Price]
    vegan: bool
    size: str
    utility: str
    size_unit: float
    hair_type: str
    hair_shaft_condition: str
    sku: str
    create_at: datetime = field(default_factory=datetime.now)
