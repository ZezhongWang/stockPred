import numpy as np
import pandas as pd
import os

writePath='/stockPred/CleanedData/'
readPath ='/bbox/data/5min'

class CleanData(object):
    # Xiao lin Huang
    
    def   clean_single_data(self , file_path):
        code_data=pd.read_csv(file_path)
        if not code_data.empty:
            time_split=pd.DataFrame((x.split(' ') for x in code_data.date),columns=['day','time'])
            code_data = code_data.drop(['date'], axis = 1)
            code_data = pd.concat([time_split, code_data], axis = 1)
            #p_change=(codeData['p_change']-codeData['p_change'].min())/(codeData['p_change'].max()-codeData['p_change'].min())
            #codeData=codeData.drop(['p_change'],axis=1)
            #codeData=codeData.insert(9,'p_change',p_change)
            try:
                code_begin_pos = file_path.rfind('/')
                code_data.to_csv(writePath+file_path[-code_begin_pos:]) 
            except AttributeError:
                pass
    
    def get_file_list(self , file_dir):
        # acquire all complete .csv file path under a file director
        file_list = []
        for root, dirs, files in os.walk(file_dir):
            for f in files:
                if os.path.splitext(f)[1] == '.csv':
                    file_list.append(os.path.join(root, f))
        return file_list
    
    def run(self , file_path_list):
        file_path_list = get_file_list(file_path)
        for file_path in file_path_list:
            clean_single_data(self , file_path)
        pass