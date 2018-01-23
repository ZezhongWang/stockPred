from preProcessor import PreProcessor
import argparse
from regression import Regression
from picDrawer import PicDrawer


if __name__ == '__main__':

    '''
    
        python run -f [filepath] -s [filepath] -c [stock code]
    
    output:
        stock error : implement by regression.score() 
        picture : implement by drawer
    
    '''

    # create pre processor

    data_cleaner = PreProcessor()
    train_feature, train_label, test_feature, test_label = data_cleaner.run()

    reg = Regression()
    reg.fit(train_feature, train_label)
    pred_result = reg.predict(test_feature)

    score = reg.score(test_label, pred_result)

    drawer = PicDrawer()
    drawer.run()



