import pandas as pd
import matplotlib.pyplot as plt


class PicDrawer(object):
    # xin Guo

    def run(self):
        csv_reader = pd.read_csv('000001.csv')
        test_label = csv_reader['p_change']

        csv_reader = pd.read_csv('000002.csv')
        predict_label = csv_reader['p_change']
        x = []
        y = []
        y2 = []
        for index, row in csv_reader.iterrows():
            x.append(row['date'])
        for index, row in predict_label.iteritems():
            y.append(row)
        for index, row in test_label.iteritems():
            y2.append(row)

        plt.plot(x, y, 'b', x, y2, 'g')
        plt.show()
