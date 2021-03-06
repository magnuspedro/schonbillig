from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

from .code import Code
from .price import Price
from .url import Url


@dataclass
class Dye:
    name: str
    brand: str
    brand_line: str
    price: List[Price]
    size: str
    utility: str
    size_unit: float
    hair_type: str
    hair_shaft_condition: str
    url: List[Url]
    code: List[Code]
    texture: Optional[str]
    products_for: List[str]
    properties: Optional[List[str]]
    control: Optional[str]
    color: Optional[str]
    volume: Optional[str]
    dyeing_type: Optional[str]
    tone: Optional[str]
    color_number: Optional[str]
    create_at: datetime = field(default_factory=datetime.now)
