import unittest

from tests.gateway.providers.beleza_na_web.converter.test_conditioner_converter \
    import TestConditionerConverter
from tests.gateway.providers.beleza_na_web.converter.test_shampoo_converter\
    import TestShampooConverter
from tests.gateway.providers.beleza_na_web.converter.test_finisher_converter \
    import TestFinisherConverter
from tests.gateway.providers.beleza_na_web.test_beleza_na_web_request_itens \
    import TestBelezaNaWebRequestItens
from tests.gateway.providers.beleza_na_web.test_beleza_na_web_spyder \
    import TestBelezaNaWebSpyder
from tests.gateway.providers.test_request import TestRequest
from tests.usecase.test_get_conditioner import TestGetConditioner
from tests.usecase.test_get_shampoo import TestGetShampoo
from tests.usecase.test_get_finisher import TestGetFinisher


def create_suite():
    test_suite = unittest.TestSuite
    test_suite.addTest(TestShampooConverter)
    # test_suite.addTest(TestConditionerConverter)
    test_suite.addTest(TestBelezaNaWebRequestItens)
    test_suite.addTest(TestBelezaNaWebSpyder)
    test_suite.addTest(TestRequest)
    test_suite.addTest(TestGetShampoo)
    test_suite.addTest(TestGetConditioner)
    return test_suite


if __name__ == "__main__":
    suite = create_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)
