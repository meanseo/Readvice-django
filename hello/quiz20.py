import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from domains import myRandom
from quiz00 import Quiz00


class Quiz20:

    def quiz20list(self) -> str:
        list1 = [1, 2, 3, 4]
        print(list1, type(list1))
        print(list1[0], list1[-1], list1[-2], list1[1:3])

        list2 = ['math', 'english']
        print(list2[0])
        print(list2[0][1])

        list3 = [1, '2', [1, 2, 3]]
        print(list3)

        list4 = [1, 2, 3]
        list5 = [4, 5]
        print(list4 + list5)
        print(2 * list4)
        list4.append(list5)
        print(list4)
        list4[-2:] = []
        print(list4)

        a = [1, 2]
        b = [0, 5]
        c = [a, b]
        print(c)
        print(c[0][1])
        c[0][1] = 10
        print(c)

        a = range(10)
        print(a)
        sum(a)

        b = [2, 10, 0, -2]
        sorted(b)

        b.index(0)
        len(b)
        print(b.index(0), len(b))

        return None

    def quiz21tuple(self) -> str:
        a = (1, 2)
        print(a, type(a))

        a[0] = 4

        a = (1, 2)
        b = (0, (1, 4))
        print(a + b)

        return None

    def quiz22dict(self) -> str:
        a = {"class": ['deep learning', 'machine learning'], "num_studuents": [40, 20]}

        type(a)

        print(a["class"])

        a['grade'] = ['A', 'B', 'C']
        print(a)

        a.keys()

        list(a.keys())

        a.values()

        a.items()

        a.get('class')

        print("class" in a)

        return None

    def quiz23listcom(self) -> str:
        print('---------- legacy ----------')
        a = []
        for i in range(5):
            a.append(i)
        print(a)
        print('------- comprehension -------')
        a2 = [i for i in range(5)]
        print(a2)
        return None


    def quiz24zip(self) -> {}:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml') # html.parser vs lxml
        # print(soup.prettify())
        # print(''.join(self.crawling(soup, input('태그명: '), input('구분: '))))
        ls1 = self.crawling(soup, 'p', 'title')
        ls2 = self.crawling(soup, 'p', 'artist')
        dict = {i: j for i, j in zip(ls1, ls2)}
        d1 = dict(zip(ls1, ls2))
        l = [i+j for i, j in zip(ls1, ls2)]
        l2 = list(zip(ls1, ls2))
        print(dict)
        print(d1)
        # self.dict1(ls1, ls2)
        # self.dict2(ls1, ls2)



    @staticmethod
    def dict1(ls1, ls2) -> None:
        dict = {}
        for i in range(0, len(ls1)):
            dict[ls1[i]] = ls2[i]
        print(dict)

    @staticmethod
    def dict2(ls1, ls2) -> None:
        dict = {}
        for i, j in enumerate(ls1):
            dict[j] = ls2[i]
        print(dict)

    @staticmethod
    def dict3(ls1, ls2) -> None:
        dict = {}
        for i, j in zip(ls1, ls2):
            dict[i] = j
        print(dict)

    def print_music_list(self, soup) -> None:
        artists = soup.find_all('p', {'class': 'artist'})
        artists = [i.get_text() for i in artists]
        print(''.join(i for i in artists))

        titles = soup.find_all('p', {'class': 'title'})
        titles = [i.get_text() for i in titles]
        print(''.join(i for i in titles))

    def find_rank(self, soup) -> None:
        '''
        for i, j in enumerate(['artist', 'title']):
            for i, j in enumerate(self.crawling(soup, j)):
               print(f'{i}위: {j}')
        '''
        for i, j in enumerate(['artist', 'title']):
            print('\n\n\n'.join(i for i in [i for i in self.crawling(soup, 'p', j)]))
            print('#'*100)


    @staticmethod
    def crawling(soup, tag, cls_nm) -> []:
        ls = soup.find_all(tag, {'class': cls_nm})
        s = [i.get_text() for i in ls]
        return s
        # return [i.get_text() for i in soup.find_all(tag, {'class': cls_nm})]

    @staticmethod
    def quiz25dictcom() -> {}:
        q = Quiz00()
        scores = [myRandom(0, 101) for i in range(5)]
        students = set([q.quiz06member_choice() for i in range(5)])
        while len(students) < 5:
            students.add(q.quiz06member_choice())
        students_res = list(students)
        dict = {i:j for i, j in zip(students_res, scores)}
        print(dict)
        return dict

    def quiz26map(self) -> str: return None

    def quiz27melon(self) -> {}:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')
        ls1 = self.find_melon(soup, 'div', 'ellipsis rank01')
        ls2 = self.find_melon(soup, 'span', 'checkEllipsis')
        dict = {}
        for i, j in zip(ls1, ls2):
            dict[i] = j
        print(dict)
        return dict

    @staticmethod
    def find_melon(soup, tag, cls_nm) -> []:
        a = soup.find_all(tag, {'class': cls_nm})
        return [i.get_text() for i in a]

    def quiz28dataframe(self) -> None:

        # dict = self.quiz24zip()
        # df = pd.DataFrame.from_dict(dict, orient='index')
        # print(df)
        # df.to_csv('./save/bugs.csv', sep=',', na_rep='NaN')

        # dict2 = self.quiz27melon()
        #df2 = pd.DataFrame.from_dict(dict2, orient='index')
        #df2.to_csv('./save/melon.csv', sep=',', na_rep='NaN')

        # df3 = Quiz30.quiz33_df_loc()
        # df3.to_csv('./save/my_grade.csv', sep=',', na_rep='NaN')

        '''
        다음 결과 출력
            a   b   c
        1   1   3   5
        2   2   4   6
        '''
    def quiz29_pandas_01(self) -> object:
        '''
        l1 = [1, 3, 5]
        l2 = [2, 4, 6]
        d1 = {'a': l1[0], 'b': l1[1], 'c': l1[2]}
        d2 = {'a': l2[0], 'b': l2[1], 'c': l2[2]}
        df = pd.DataFrame.from_dict([d1])
        df1 = pd.DataFrame.from_dict(d1, orient='index')
        print(df)
        print('#'*100)
        '''

        #d = {'1': [1, 3, 5], '2': [2, 4, 6]}
        #df = pd.DataFrame.from_dict(d, orient='index', columns=['a', 'b', 'c'])

        columns = [chr(i) for i in range(97, 100)]
        a1 = []
        a2 = []
        [a1.append(i) if i % 2 == 1 else a2.append(i) for i in range(1, 7)]

        e = ['1', '2']
        f = [a1, a2]
        d = {i: j for i, j in zip(e, f)}
        df = pd.DataFrame.from_dict(d, orient='index', columns=columns)
        print(df)
        return df