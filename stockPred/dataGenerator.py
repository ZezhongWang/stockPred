import os
import pandas as pd
from util import *

class DataGenerator(object):
    # ze zhong wang
    def __init__(self, file_path, code):
        self.file_path = file_path
        self.code = code
        self.file_list = self.get_file_list(file_path)

    def run(self):
        
        return train_feature, train_label, test_feature, test_label