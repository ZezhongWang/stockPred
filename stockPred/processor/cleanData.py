import numpy as np
import pandas as pd
import os

writePath='/stockPred/CleanedData/'
readPath ='/bbox/data/5min'

class CleanData(object):
    # Xiao lin Huang
    
    def   clean(self , path):
        codeData=pd.read_csv(path)
    
        codeData=codeData.dropna()
    
        dataSplit=pd.DataFrame((x.split('-') for x in codeData.date),columns=['year','month','day'])
        codeData=codeData.drop(['date'],axis=1)
        year=dataSplit.pop('year')
        day=dataSplit.pop('day')
        month=dataSplit.pop('month')
        codeData.insert(0,'year',year)
        codeData.insert(1,'month',month)
        codeData.insert(2,'day',day)
    
        p_change=(codeData['p_change']-codeData['p_change'].min())/(codeData['p_change'].max()-codeData['p_change'].min())
        codeData=codeData.drop(['p_change'],axis=1)
        codeData=codeData.insert(9,'p_change',s)
        codeData.to_csv(writePath+path[-10:]) 
    
    def run(self):
        files = os.listdir(readPath)
        for f in files:
            clean(self,f)
        pass