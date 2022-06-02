# https://github.com/datasciencedojo/datasets/blob/master/titanic.csv
from titanic.models import TitanicModel
from titanic.templates import TitanicTemplate
from titanic.views import TitanicView

if __name__ == '__main__':
    view = TitanicView()

    while 1:
        menu = input('1.템플릿 2.전처리')
        if menu == '1':
            print(' #### 1. 템플릿 #### \n')
            template = TitanicTemplate(fname='train.csv')
            # view.preprocess('train.csv', 'test.csv')
            template.visualize()
            break
        elif menu == '2':
            print(' #### 2. 전처리 #### \n')
            model = TitanicModel()
            model.learning(train_fname='train.csv',
                                 test_fname='test.csv')
            break