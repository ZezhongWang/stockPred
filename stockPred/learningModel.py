from sklearn import linear_model


class LearningModel(object):

    def __init__(self, method='LinearRegression'):
        self._method = method
        if method == 'LinearRegression':
            self.reg = linear_model.LinearRegression()

    def fit(self, train_data, train_label):
        self.reg.fit(train_data, train_label)

    def predict(self, test_data):
        pred_label = self.reg.predict(test_data)
        return pred_label

    def score(self, train_data, test_label):
        score = self.reg.score(train_data, test_label)
        return score
