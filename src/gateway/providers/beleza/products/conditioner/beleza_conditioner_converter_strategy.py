from src.entrypoints.converter.beleza_get_conditioner_conevert \
    import BelezaGetConditionerConverter


class BelezaConditionerConverterStrategy:

    @staticmethod
    def convert(response):
        return BelezaGetConditionerConverter().to_entity(response)
