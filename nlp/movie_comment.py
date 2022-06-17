import math

import numpy as np
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import icecream as ic
from pandas._libs.internals import defaultdict

from context.domains import Reader, File
from matplotlib import pyplot as plt
from matplotlib import rc, font_manager
rc('font', family=font_manager.FontProperties(fname='C:/Windows/Fonts/malgunsl.ttf').get_name())
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False

'''
출처: https://prlabhotelshoe.tistory.com/20?category=1003351
'''
# ML 구조
class Solution(Reader):
    def __init__(self, k=0.5):
        self.movie_comment = pd.DataFrame()
        self.file = File()
        self.file.context = './data/'
        self.k = k
        self.word_probs = []

    def hook(self):
        def print_menu():
            print('0. Exit')
            print('1. 전처리: 데이터 마이닝(크롤링)')
            print('2. 전처리: 정형화 ')
            print('3. 다음 영화 댓글이 긍정인지 부정인지 ratio 값으로 판단하시오 \n '
                  '너무 좋아요. 내 인생의 최고의 명작 영화\n'
                  '이렇게 졸린 영화는 처음이야')
            print('3. 임베딩 ')
            return input('메뉴 선택 \n')

        while 1:
            menu = print_menu()
            if menu == '0':
                break
            elif menu == '1':
                self.crawling()
            elif menu == '2':
                self.preprocess()
            elif menu == '3':
                doc = '이런 개쓰레기 같은 영화, 다시는 안보고 싶다. 돈 아까움'
                self.naive_bayes_classifier(doc)
                doc = '너무 좋아요. 내 인생의 최고의 명작 영화'
                self.naive_bayes_classifier(doc)
                doc = '이렇게 졸리고 거지같은 내용의 영화는 처음이야'
                self.naive_bayes_classifier(doc)


    def preprocess(self):
        self.stereotype()
        df = self.movie_comments
        # ic(df.head())
        df = df.dropna()
        df = df.drop_duplicates(['comment'])
        # self.reviews_info(df)
        df.label.value_counts()
        top10 = self.top10_movies(df)
        avg_score = self.get_avg_score(top10)
        self.visualization(avg_score, top10)

    def crawling(self):
        file = self.file
        file.fname = 'movie_reviews.txt'
        path = file
        f = open('save/movie_reviews.txt', 'w', encoding='UTF-8')
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
        file.context = './save/'
        file.fname = 'movie_reviews.txt'
        path = self.new_file(file)
        self.movie_comments = pd.read_csv(path, delimiter='\t',
                                          names=['title', 'score', 'comment', 'label'])
        # 리턴 안하고 전역으로 뺌

    def reviews_info(self, df):
        movie_lst = df.title.unique()
        ic('전체 영화 편수 =', len(movie_lst))
        ic(movie_lst[:10])
        cnt_movie = df.title.value_counts()
        ic(cnt_movie[:20])
        # info_movie = df.groupby('title')['score'].describe() 한 번만 쓰기 때문에 lambda 로 변환
        ic((lambda a, b: df.groupby(a)[b].describe())('title', 'score').sort_values(by=['count'], axis=0,ascending=False))

    def top10_movies(self, df):
        top10 = df.title.value_counts().sort_values(ascending=False)[:10]
        top10_title = top10.index.tolist()
        return df[df['title'].isin(top10_title)]

    def get_avg_score(self, top10):
        movie_title = top10.title.unique().tolist()  # -- 영화 제목 추출
        avg_score = {}  # -- {제목 : 평균} 저장
        for t in movie_title:
            avg = top10[top10['title'] == t]['score'].mean()
            avg_score[t] = avg
        return avg_score

    def visualization(self, avg_score, top10):
        plt.figure(figsize=(10, 5))
        plt.title('영화 평균 평점 (top 10: 리뷰 수)\n', fontsize=17)
        plt.xlabel('영화 제목')
        plt.ylabel('평균 평점')
        plt.xticks(rotation=20)

        for x, y in avg_score.items():
            color = np.array_str(np.where(y == max(avg_score.values()), 'orange', 'lightgrey'))
            plt.bar(x, y, color=color)
            plt.text(x, y, '%.2f' % y,
                     horizontalalignment='center',
                     verticalalignment='bottom')

        plt.show()
        self.rating_distribution(avg_score, top10)
        self.circle(avg_score, top10)

    def rating_distribution(self, avg_score, top10):
        fig, axs = plt.subplots(5, 2, figsize=(15, 25))
        axs = axs.flatten()

        for title, avg, ax in zip(avg_score.keys(), avg_score.values(), axs):
            num_reviews = len(top10[top10['title'] == title])
            x = np.arange(num_reviews)
            y = top10[top10['title'] == title]['score']
            ax.set_title('\n%s (%d명)' % (title, num_reviews), fontsize=15)
            ax.set_ylim(0, 10.5, 2)
            ax.plot(x, y, 'o')
            ax.axhline(avg, color='red', linestyle='--')  # -- 평균 점선 나타내기

        plt.show()

    def circle(self, avg_score, top10):
        fig, axs = plt.subplots(5, 2, figsize=(15, 25))
        axs = axs.flatten()
        colors = ['pink', 'gold', 'whitesmoke']
        labels = ['1 (8~10점)', '0 (1~4점)', '2 (5~7점)']

        for title, ax in zip(avg_score.keys(), axs):
            num_reviews = len(top10[top10['title'] == title])
            values = top10[top10['title'] == title]['label'].value_counts()
            ax.set_title('\n%s (%d명)' % (title, num_reviews), fontsize=15)
            ax.pie(values,
                   autopct='%1.1f%%',
                   colors=colors,
                   shadow=True,
                   startangle=90)
            ax.axis('equal')
        plt.show()

    def naive_bayes_classifier(self, doc):
        training_set = self.load_corpus()
        # print(training_set)
        counts = self.count_word(training_set)
        # print(counts)
        self.train()
        self.classify(doc)

    def load_corpus(self):
        file = self.file
        file.context = './save/'
        file.fname = 'movie_reviews.txt'
        path = self.new_file(file)
        corpus = pd.read_table(path, encoding='UTF-8', names=['title', 'point', 'doc', 'label'])
        corpus.drop(columns=['title', 'label'], inplace=True)
        corpus = np.array(corpus)
        return corpus

    def count_word(self, training_set):
        counts = defaultdict(lambda: [0, 0])
        for point, doc in training_set:
            # 영화리뷰가 text 일때만 카운드
            if self.isNumber(doc) is False:
                # 리뷰를 띄어쓰기 단위로 토크나이징
                words = doc.split()
                for word in words:
                    counts[word][0 if point > 8 else 1] += 1
        return counts

    def isNumber(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def word_probabilities(self, counts, total_class0, total_class1, k):
        """pass"""
        # 단어의 빈도수를 [단어, p(w|긍정), p(w|부정)] 형태로 변환
        return [(w, (class0 + k) / (total_class0 + 2 * k), (class1 + k) / (total_class1 + 2 * k)) for
                w, (class0, class1) in counts.items()]

    def class0_probabilties(self, word_probs, doc):
        # 별도 토크나이즈 하지 않고 띄어쓰기만
        docwords = doc.split()
        # 초기값은 모두 0으로 처리
        log_prob_if_class0 = log_prob_if_class1 = 0.0
        # 모든 단어에 대해 반복
        for word, prob_if_class0, prob_if_class1 in word_probs:
            # 만약 리뷰에 word 가 나타나면 해당 단어가 나올 log 에 확률을 더 해줌
            if word in docwords:
                log_prob_if_class0 += math.log(prob_if_class0)
                log_prob_if_class1 += math.log(prob_if_class1)
            # 만약 리뷰에 word 가 나타나지 않는다면
            # 해당 단어가 나오지 않을 log 에 확률을 더해줌
            # 나오지 않을 확률은 log(1 - 나올 확률) 로 계산
            else:
                log_prob_if_class0 += math.log(1.0 - prob_if_class0)
                log_prob_if_class1 += math.log(1.0 - prob_if_class1)
        prob_if_class0 = math.exp(log_prob_if_class0)
        prob_if_class1 = math.exp(log_prob_if_class1)
        return print(prob_if_class0 / (prob_if_class0 + prob_if_class1))

    def train(self):
        print('-------------- 훈련 시작 --------')
        training_set = self.load_corpus()
        # 범주0 (긍정) 과 범주1(부정) 문서의 수를 세어줌
        num_class0 = len([1 for point, _ in training_set if point > 8])
        num_class1 = len(training_set) - num_class0
        # train
        word_counts = self.count_word(training_set)
        # print(word_counts)
        self.word_probs = self.word_probabilities(word_counts, num_class0, num_class1, self.k)

    def classify(self, doc):
        return self.class0_probabilties(self.word_probs, doc)

    def tokenization(self):
        pass

    def embedding(self):
        pass

if __name__ == '__main__':
    Solution().hook()