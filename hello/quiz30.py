import random
import string
import numpy as np
import pandas as pd
from icecream import ic
from hello.domains import members
from context.models import Model


class Quiz30:
    '''
                데이터프레임 문제 Q02
            ic| df:     A   B   C
                    1   1   2   3
                    2   4   5   6
                    3   7   8   9
                    4  10  11  12
    '''
    def quiz30_df_4_by_3(self) -> object:
        a = [[i for i in range(j * 3 + 1, j * 3 + 4)] for j in range(4)]
        df = pd.DataFrame(a, index=range(1, 5), columns=['A', 'B', 'C'])

        # 위 식을 리스트 결합 형태로 분해해서 조립하시오
        d = {'1': range(1, 4),
             '2': range(4, 7),
             '3': range(7, 10),
             '4': range(10, 13)} # {'1': [i for i in range(1, 4)]}
        df2 = pd.DataFrame.from_dict(d, orient="index", columns=['A', 'B', 'C'])

        ic(df)
        return None

    '''
        데이터프레임 문제 Q03.
        두자리 정수를 랜덤으로 2행 3열 데이터프레임을 생성
        ic| df:     0   1   2
                0  97  57  52
                1  56  83  80
    '''
    def quiz31(self) -> object:
        '''
        ls = [[myRandom(10, 100) for i in range(3)] for i in range(2)]
        df = pd.DataFrame(ls)
        '''

        # 넘파이 사용 예제
        df = pd.DataFrame(np.random.randint(10, 100, size=(2, 3)))
        ic(df)
        return df

    '''
        데이터프레임 문제 Q04.
        국어, 영어, 수학, 사회 4과목을 시험 치른 10명의 학생들의 성적표 작성.
            (단, 점수 0 ~ 100이고 학생은 랜덤 알파벳 5자리 ID 로 표기)

            ic| df4:        국어  영어  수학  사회
                        lDZid  57  90  55  24
                        Rnvtg  12  66  43  11
                        ljfJt  80  33  89  10
                        ZJaje  31  28  37  34
                        OnhcI  15  28  89  19
                        claDN  69  41  66  74
                        LYawb  65  16  13  20
                        QDBCw  44  32   8  29
                        PZOTP  94  78  79  96
                        GOJKU  62  17  75  49
    '''
    def quiz32_df_grade(self) -> object:
        col = ['국어', '영어', '수학', '사회']
        idx = [self.get_id(5) for i in range(10)]
        data = np.random.randint(0, 100, (10, 4))
        df1 = pd.DataFrame(data, index=idx, columns=col)
        d = {i: j for i, j in zip(idx, data)}
        df2 = pd.DataFrame.from_dict(d, orient='index', columns=col)
        ic(df1)
        ic(df2)
        return None

    @staticmethod
    def get_id(chr_size) -> str: return ''.join([random.choice(string.ascii_letters) for i in range(chr_size)])

    @staticmethod
    def quiz33_df_loc() -> None:
        # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html

        subj = ['자바', '파이썬', '자바스크립트', 'SQL']
        stud = members()
        score = np.random.randint(0, 100, (24, 4))
        students_scores_df = pd.DataFrame(score, index=stud, columns=subj)
        # grade.csv
        model = Model()
        model.save_model(fname='grade.csv', dframe=students_scores_df)
        grade_df = model.new_model('grade.csv')
        ic(grade_df)
        print('파이썬의 점수만 출력하시오')
        python_scores = grade_df.loc[:, '파이썬']
        ic(type(python_scores))
        ic(python_scores)
        print('조현국의 점수만 출력하시오')
        cho_score = grade_df.loc['조현국']
        ic(type(cho_score))
        ic(cho_score)
        print('조현국의 과목별 점수를 출력하시오')
        cho_subjects_scores = grade_df.loc[['조현국']]
        ic(cho_subjects_scores)
        ic(type(cho_subjects_scores))

    @staticmethod
    def creat_df(keys, vals, len) -> object:
        return pd.DataFrame([dict(zip(keys, vals)) for _ in range(len)])

    def quiz34_df_iloc(self) -> str:
        # d = [{i: j for i, j in zip(['a', 'b', 'c', 'd'], np.random.randint(0, 100, 4))} for _ in range(3)]
        # d = [dict(zip(['a', 'b', 'c', 'd'], np.random.randint(0, 100, 4))) for _ in range(3)]
        df1 = self.creatDf(keys=['a', 'b', 'c', 'd'],
                             vals=np.random.randint(0, 100, 4),
                             len=3)
        # ic(df1)

        # ic(df.iloc[0])
        '''
        ic| df.iloc[0]: a     0
                b    65
                c     1
                d    48
                Name: 0, dtype: int32
        '''
        # ic(df.iloc[[0]])
        '''
        ic| df.iloc[[0]]:     a   b   c   d
                           0  68  10  59  53
        '''
        # ic(df.iloc[[0,1]])
        '''
        ic| df.iloc[[0,1]]:     a  b  c   d
                            0  38  2  7  36
                            1  38  2  7  36

        '''
        # ic(df.iloc[:3])
        '''
        ic| df.iloc[:3]:   a   b   c   d
                        0  27  33  21  59
                        1  27  33  21  59
                        2  27  33  21  59
        '''
        # ic(df.iloc[[True, False, True]])
        '''
        ic| df.iloc[[True, False, True]]:      a   b   c   d
                                            0  89  94  76  28
                                            2  89  94  76  28
        '''
        # ic(df.iloc[lambda x: x.index % 2 == 0])
        '''
        ic| df.iloc[lambda x: x.index % 2 == 0]:    a  b   c   d
                                                0  26  1  34  31
                                                2  26  1  34  31
        '''
        # ic(df.iloc[0, 1])
        '''
        ic| df.iloc[0, 1]: 7
        '''

        # ic(df.iloc[1:3, 0:3])
        '''
        ic| df.iloc[1:3, 0:3]:     a   b   c
                                1  15  42  38
                                2  15  42  38
        '''
        # ic(df.iloc[:, [True, False, True, False]])
        '''
        ic| df.iloc[:, [True, False, True, False]]:     a   c
                                                    0  64  86
                                                    1  64  86
                                                    2  64  86
        '''
        # ic(df.iloc[:, lambda df: [0, 2]])
        '''
        ic| df.iloc[:, lambda df: [0, 2]]:     a   c
                                            0  63  46
                                            1  63  46
                                            2  63  46
        '''
        return None

    def quiz35(self) -> str: return None

    def quiz36(self) -> str: return None

    def quiz37(self) -> str: return None

    def quiz38(self) -> str: return None

    def quiz39(self) -> str: return None