import os
import pandas as pd
from util import *

class DataGenerator(object):
    # ze zhong wang
    def __init__(self, file_path, code, test_set_ratio):
        self.file_path = file_path
        self.code = code
        self.test_set_ratio = test_set_ratio
        self.file_list = get_file_list(file_path)
        self.stocks_data_dict = load_all_data(self.file_list)

    def get_code_data_set(self, code, ahead_num=11):
        origin_df = self.stocks_data_dict[code]
        data_set = []
        for index in range(len(origin_df) - ahead_num):
            row = origin_df.iloc[index]
            day = row['date'][8:10]
            row_ahead = origin_df.iloc[index + ahead_num]
            day_ahead = row_ahead['date'][8:10]
            # ensure that the ahead data is in the same day
            # but we don't guarantee that the features and label
            # are in the same afternoon or morning
            if day_ahead == day:
                features = list(origin_df.iloc[range(index + 1, ahead_num + index + 1)]['p_change'])
                features.append(row['date'])
                label = float(row['p_change'])
                features.append(label)
                data_set.append(features)
        return pd.DataFrame(data_set)

    def train_test_split(self, data_set):
        num = len(data_set)
        data_set_columns = data_set.columns
        feature_columns = data_set_columns[:-1]
        # assume that label always is the last columns
        label_columns = data_set_columns[-1]
        test_num = int(num * self.test_set_ratio)
        # train data part
        train_data = data_set[:-test_num]
        train_feature = train_data[feature_columns]
        train_label = train_data[label_columns]
        # test data part
        test_data = data_set[-test_num:].reset_index(drop=True)
        test_feature = test_data[feature_columns]
        test_label = test_data[label_columns]
        return train_feature, train_label, test_feature, test_label

    def run(self):

        code_data = load_data(os.path.join(self.file_path, self.code+'.csv'))
        train_feature, train_label, test_feature, test_label = self.train_test_split(code_data)
        return train_feature, train_label, test_feature, test_label
