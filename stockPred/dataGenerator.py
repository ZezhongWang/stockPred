import os
import pandas as pd
from util import *

class DataGenerator(object):
    # ze zhong wang
    def __init__(self, file_path, code):
        self.file_path = file_path
        self.code = code
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

    def run(self):
        
        return train_feature, train_label, test_feature, test_label