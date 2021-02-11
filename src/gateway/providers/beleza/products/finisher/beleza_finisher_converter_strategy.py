from src.entrypoints.converter.beleza_get_finisher_converter \
    import BelezaGetFinisherConverter


class BelezaFinisherConverterStrategy:

    @staticmethod
    def convert(response):
        return BelezaGetFinisherConverter().to_entity(response)
