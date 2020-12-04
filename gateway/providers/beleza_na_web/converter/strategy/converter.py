from enum import Enum

from .shampoo_converter_strategy import ShampooConverterStrategy


class Converter(Enum):
    SHAMPOO = ShampooConverterStrategy()
