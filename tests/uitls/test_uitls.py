from dataclasses import asdict

from src.entities.conditioner import Conditioner
from src.utils.utils import Utils



def test_del_none(mocker):
    conditioner = Conditioner(name='Wella Professionals Fusion',
                              price='555.059,90',
                              brand='Wella Professionals',
                              brand_line=None,
                              hair_type=None,
                              size_unit='Miniatura',
                              utility=None,
                              hair_shaft_condition='Quebradiços',
                              size=None,
                              url=None,
                              code=None,
                              properties=None,
                              control=None,
                              texture='Liquido')
    conditioner_dict = asdict(conditioner)
    conditioner_dict = Utils.del_none(conditioner_dict)
    print(conditioner_dict)
    print(conditioner_dict)
    assert type(conditioner_dict) is dict




