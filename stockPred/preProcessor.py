from processor.calcCorrMatrix import CalcCorrMatrix
from processor.cleanData import CleanData
from dataGenerator import DataGenerator


class PreProcessor(object):

    def run(self):
        clean_data = CleanData()
        clean_data.run()

        calc_corr = CalcCorrMatrix()
        calc_corr.run()

        data_generator = DataGenerator()
        train_feature, train_label, test_feature, test_label = data_generator.run()

        return train_feature, train_label, test_feature, test_label


