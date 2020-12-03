from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Price:
    price: float
    create_at: datetime = field(default_factory=datetime.now)
