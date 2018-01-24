# -*- coding: utf-8 -*-
__author__ = 'w2w'
__date__ = '18-1-24 下午7:08'
from sklearn import preprocessing


class LabelEncoder(object):
    def __init__(self):
        self.label_encoder = preprocessing.LabelEncoder()

    def transform(self, y):
        y_ = self.label_encoder.fit_transform(y)
        return y_

    def inverse_transform(self, y):
        y_ = self.label_encoder.inverse_transform(y)
        return y_


# class MinMaxScaler(object):
#     def __init__(self):
#         self.scalar = preprocessing.MinMaxScaler()
#
#     def transform(self, y):
#