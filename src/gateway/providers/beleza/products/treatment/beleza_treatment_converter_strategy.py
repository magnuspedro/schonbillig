from src.entrypoints.converter.beleza_get_treatment_converter \
    import BelezaGetTreatmentConverter


class BelezaTreatmentConverterStrategy:

    @staticmethod
    def convert(response):
        return BelezaGetTreatmentConverter().to_entity(response)
