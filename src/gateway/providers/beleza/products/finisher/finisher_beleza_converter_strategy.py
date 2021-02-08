from src.entrypoints.converter.get_finisher_beleza_converter \
    import GetFinisherBelezaConverter


class FinisherBelezaConverterStrategy:

    @staticmethod
    def convert(response):
        return GetFinisherBelezaConverter().to_entity(response)
