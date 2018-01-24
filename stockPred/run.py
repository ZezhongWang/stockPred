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
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", type=str, help="the directory of the .csv file")
    parser.add_argument("code", type=int, help="the stock code you want to predict")
    parser.add_argument("-r", "--ratio", type=float,
                        default=0.1, help="the validate data set ratio")
    parser.add_argument("-p", "--preprocess", type=bool, help="preprocessing or not",
                        default=True)
    args = parser.parse_args()

    file_path = args.filepath

    # create pre processor
    if args.p == True:
        data_cleaner = PreProcessor(file_path)
        train_feature, train_label, test_feature, test_label = data_cleaner.run()

    reg = Regression()
    reg.fit(train_feature, train_label)
    pred_result = reg.predict(test_feature)

    score = reg.score(test_label, pred_result)

    drawer = PicDrawer()
    drawer.run()



