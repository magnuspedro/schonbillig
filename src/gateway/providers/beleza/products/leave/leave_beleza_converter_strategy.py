from src.gateway.providers.beleza.converter.get_leave_beleza_converter \
    import GetLeaveBelezaConverter


class LeaveBelezaConverterStrategy:

    @staticmethod
    def convert(response):
        return GetLeaveBelezaConverter().to_entity(response)