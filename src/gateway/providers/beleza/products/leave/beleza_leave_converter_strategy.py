from src.entrypoints.converter.beleza_get_leave_converter \
    import BelezaGetLeaveConverter


class BelezaLeaveConverterStrategy:

    @staticmethod
    def convert(response):
        return BelezaGetLeaveConverter().to_entity(response)
