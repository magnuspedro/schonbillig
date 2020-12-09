from src.gateway.providers.beleza_na_web.converter.get_conditioner_beleza_conevert\
    import GetConditionerBelezaConverter


class ConditionerBelezaConverterStrategy():

    def convert(self, response):
        return GetConditionerBelezaConverter().to_entity(response)
