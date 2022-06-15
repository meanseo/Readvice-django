from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import icecream as ic

from context.domains import Reader, File

'''
출처: https://prlabhotelshoe.tistory.com/20?category=1003351
'''
class Solution(Reader):
    def __init__(self):
        self.movie_comment = pd.DataFrame()
        self.file = File()
        self.file.context = './data/'

    def hook(self):
        def print_menu():
            print('0. Exit')
            print('1. driver를 이용한 크롤링 후 코멘트 파일 생성.')
            print('2. 정형화 ')
            print('3. 토큰화 ')
            print('3. 임베딩 ')
            return input('메뉴 선택 \n')

        while 1:
            menu = print_menu()
            if menu == '0':
                break
            if menu == '1':
                self.crawling()
            if menu == '2':
                self.preprocess()
            elif menu == '3':
                break

    def preprocess(self):
        self.stereotype()
        ic(self.movie_comments.head(5))
        ic(self.movie_comments)

    def tokenization(self):
        pass

    def embedding(self):
        pass

    def crawling(self):
        file = self.file
        file.fname = 'movie_reviews.txt'
        path = file
        f = open('./data/movie_reviews.txt', 'w', encoding='UTF-8')
        # -- 500페이지까지 크롤링
        for no in range(1, 501):
            url = 'https://movie.naver.com/movie/point/af/list.naver?&page=%d' % no
            html = urllib.request.urlopen(url)
            soup = BeautifulSoup(html, 'html.parser')

            reviews = soup.select('tbody > tr > td.title')
            for rev in reviews:
                title = rev.select_one('a.movie').text.strip()
                score = rev.select_one('div.list_netizen_score > em').text.strip()
                comment = rev.select_one('br').next_sibling.strip()

                # -- 긍정/부정 리뷰 레이블 설정
                if int(score) >= 8:
                    label = 1  # -- 긍정 리뷰 (8~10점)
                elif int(score) <= 4:
                    label = 0  # -- 부정 리뷰 (0~4점)
                else:
                    label = 2

                f.write(f'{title}\t{score}\t{comment}\t{label}\n')
        f.close()

    def stereotype(self):
        file = self.file
        file.fname = 'movie_reviews.txt'
        path = self.new_file(file)
        self.movie_comments = pd.read_csv(path, delimiter='\t',
                                          names=['title', 'score', 'comment', 'label'])
        '''
                                     title  ...  label
        0                       그대가 조국  ...      0
        1                 쥬라기 월드: 도미니언  ...      1
        2  마녀(魔女) Part2. The Other One  ...      1
        3                      두 번째 스물  ...      1
        4  마녀(魔女) Part2. The Other One  ...      0
        5             부에노스 아이레스 제로 디그리  ...      1
        6                        범죄도시2  ...      1
        7  마녀(魔女) Part2. The Other One  ...      1
        8                     버즈 라이트이어  ...      1
        9  마녀(魔女) Part2. The Other One  ...      1
        '''
        # 리턴 안하고 전역으로 뺌

    def remove_data(self):
        df_data = self.stereotype()
        # df_data.info()
        '''
                <class 'pandas.core.frame.DataFrame'>
        RangeIndex: 5000 entries, 0 to 4999
        Data columns (total 4 columns):
         #   Column   Non-Null Count  Dtype 
        ---  ------   --------------  ----- 
         0   title    5000 non-null   object
         1   score    5000 non-null   int64 
         2   comment  4684 non-null   object
         3   label    5000 non-null   int64 
        dtypes: int64(2), object(2)
        memory usage: 156.4+ KB
        '''
        # 전체 리뷰 수 확인, 전체리뷰와 평점은 5000, 하지만 코멘트는 4684
        # 코멘트가 없는 리뷰 데이터(NaN) 제거
        df_reviews = df_data.dropna()
        # 중복 리뷰 제거
        df_reviews = df_reviews.drop_duplicates(['comment'])

        df_reviews.info()
        '''
                [10 rows x 4 columns]
        <class 'pandas.core.frame.DataFrame'>
        Int64Index: 4649 entries, 0 to 4999
        Data columns (total 4 columns):
         #   Column   Non-Null Count  Dtype 
        ---  ------   --------------  ----- 
         0   title    4649 non-null   object
         1   score    4649 non-null   int64 
         2   comment  4649 non-null   object
         3   label    4649 non-null   int64 
        dtypes: int64(2), object(2)
        memory usage: 181.6+ KB
        '''
        # 코멘트 없는 리뷰와 중복 리뷰 제거 후 총 리뷰 4649로 축소
        # df_reviews.head(10)
        return df_reviews

    def comment_count(self):
        df_reviews = self.remove_data()
        movie_lst = df_reviews.title.unique()
        print('전체 영화 편수 =', len(movie_lst))
        print(movie_lst[:10])
        '''
        전체 영화 편수 = 803
        ['그대가 조국' '쥬라기 월드: 도미니언' '마녀(魔女) Part2. The Other One' '두 번째 스물'
         '부에노스 아이레스 제로 디그리' '범죄도시2' '버즈 라이트이어' '실종' '다크 나이트 라이즈' '라스베가스를 떠나며']
        '''
        # 각 영화 리뷰 수 계산
        cnt_movie = df_reviews.title.value_counts()
        print(cnt_movie[:10])
        '''
        브로커                               1326
        범죄도시2                              684
        마녀(魔女) Part2. The Other One        500
        쥬라기 월드: 도미니언                       265
        그대가 조국                             151
        버즈 라이트이어                            90
        인터셉터                                64
        닥터 스트레인지: 대혼돈의 멀티버스                 50
        피는 물보다 진하다                          44
        애프터 양                               38
        '''
        info_movie = df_reviews.groupby('title')['score'].describe()
        print(info_movie.sort_values(by=['count'], axis=0, ascending=False))
        print(df_reviews.label.value_counts())



if __name__ == '__main__':
    Solution().comment_count()
    Solution().hook()