from src.entrypoints.converter.get_treatment_beleza_converter \
    import GetTreatmentBelezaConverter


class TreatmentBelezaConverterStrategy:

    @staticmethod
    def convert(response):
        return GetTreatmentBelezaConverter().to_entity(response)
