import os
from util import load_data
import matplotlib.pyplot as plt
import seaborn as sns


class PicDrawer(object):
    def __init__(self, file_path, code, train_label, test_label, pred_label):
        file_name = code + '.csv'
        self.code = code
        self.file_path = os.path.join(file_path, file_name)
        self.train_label = list(train_label)
        self.test_label = list(test_label)
        self.pred_label = list(pred_label)

    def draw_p_change_line_chart(self):
        sns.set()
        # stock_data = load_data(self.file_path)
        true_label = self.train_label + self.test_label
        length = len(self.train_label) + len(self.test_label)
        test_length = len(self.test_label)
        plt.figure(1)
        plt.plot(range(length), true_label, 'o-', label='p_change_true')
        plt.plot(range(length-test_length, length), self.pred_label, 'o:', label='p_change_predict')
        plt.legend()
        plt.xlabel('time')
        plt.ylabel('p_change')
        plt.title("Complete Stock "+self.code+" p_change line chart")
        file_name = self.code + '.png'
        plt.savefig(os.path.join('picture', file_name))
        plt.figure(2)
        plt.plot(range(length - test_length, length), self.test_label, 'o-', label='p_change_true')
        plt.plot(range(length - test_length, length), self.pred_label, 'o:', label='p_change_predict')
        plt.legend()
        plt.xlabel('time')
        plt.ylabel('p_change')
        plt.title("Part Stock " + self.code + " p_change line chart")
        pfile_name = self.code + 'p.png'
        plt.savefig(os.path.join('picture', pfile_name))

    def run(self):
        self.draw_p_change_line_chart()


