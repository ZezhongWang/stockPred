from preProcessor import PreProcessor
import argparse
from learningModel import LearningModel
from picDrawer import PicDrawer
from dataGenerator import DataGenerator

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
    parser.add_argument("-p", "--preprocess", help="preprocessing or not",action='store_true')
    args = parser.parse_args()

    file_path = args.filepath
    code = str(args.code)
    # create pre processor
    print args.preprocess
    if args.preprocess:
        data_cleaner = PreProcessor(file_path)
        data_cleaner.run()

    data_generator = DataGenerator(file_path, code)
    train_feature, train_label, test_feature, test_label = data_generator.run()
    reg = LearningModel()
    reg.fit(train_feature, train_label)
    pred_result = reg.predict(test_feature)
    # print type(pred_result)
    # print type(test_label)

    score = reg.score(test_feature, test_label)
    print score
    #
    # # score = reg.score(test_label, pred_result)
    #
    # drawer = PicDrawer()
    # drawer.run()



