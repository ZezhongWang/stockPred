from processor.calcCorrMatrix import CalcCorrMatrix
from processor.cleanData import CleanData


class PreProcessor(object):

    def __init__(self, file_path):
        self.file_path = file_path

    def run(self):
        clean_data = CleanData(self.file_path)
        clean_data.run()

        data_transformer = DataTransformer()

        # calc_corr = CalcCorrMatrix()
        # calc_corr.run()


