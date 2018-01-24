import os
import pandas as pd

'''

        input: file path: read data

        output: stock pairs with correlations abs greater than 0.3

'''


class CalcCorrMatrix(object):
    # Jia heng Li

    def run(self, filepath):
        corr_pairs = []
        stock_panel = self.readfiles(filepath)

        stock_panel = self.del_empty_frame(stock_panel)

        # calculate correlations and get correlate pairs
        key = ['p_change']
        for key_iter in range(len(key)):
            compare = []
            for item, value in stock_panel.iteritems():
                compare.append(value[key[key_iter]].tolist())
            compare_frame = pd.DataFrame(compare)
            compare_frame = compare_frame.transpose()
            corr = compare_frame.corr()
            corr = pd.DataFrame(corr.values, index=stock_panel.items, columns=stock_panel.items)
            corr = corr[corr.abs() >= 0.3]
            corr = corr.dropna(axis=1, how='all').dropna(axis=0, how='all')
            for index, items in corr.iterrows():
                for columns in items.index:
                    if abs(items[columns]) > 0:
                        corr_pairs.append([items, columns, items[columns]])

        return corr_pairs

    def readfiles(self, filepath):
        path = os.walk(filepath)
        root = ""
        files = []
        for root_path, dirs, contained_files in path:
            root = root_path
            files = contained_files

        stock_dict = {}
        for one_file in files:
            stock_data = pd.read_csv(root + '/' + one_file)
            if stock_data.empty:
                continue
            stock_code = one_file.split('.')[0]
            stock_dict[stock_code] = stock_data
        stock_panel = pd.Panel(stock_dict)

        return stock_panel

    def del_empty_frame(self, stock_panel):
        # delete empty data
        for item, value in stock_panel.iteritems():
            stock_frame = stock_panel[item]
            stock_frame = stock_frame.dropna(axis=1, how='all')
            if len(stock_frame.columns) == 0:
                stock_panel = stock_panel.drop([item], axis=0)

        return stock_panel