from src.entrypoints.converter.get_conditioner_beleza_conevert \
    import GetConditionerBelezaConverter


class ConditionerBelezaConverterStrategy:

    @staticmethod
    def convert(response):
        return GetConditionerBelezaConverter().to_entity(response)
