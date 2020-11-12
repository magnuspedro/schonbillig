from dataclasses import dataclass


@dataclass
class Shampoo:
    name: str
    brand: str
    brand_line: str
    price: float
    vegan: bool
    size: str
    utility: str
    size_unit: float
    hair_type: str
    sku: str
