from src.gateway.providers.beleza_na_web.converter.get_finisher_beleza_converter \
    import GetFinisherBelezaConverter


class FinisherBelezaConverterStrategy():

    def convert(self, response):
        return GetFinisherBelezaConverter().to_entity(response)
