from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
import nltk
import re
import pandas as pd
from nltk import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from icecream import ic


from context.domains import File, Reader
'''
1. Preprocessing
2. Tokenization
3. Token Embedding
4. Document Embedding
'''
class Solution(Reader):
    def __init__(self):
        self.okt = Okt()
        self.file = File()
        self.file.context = './data/'

    def hook(self):
        def print_menu():
            print('0. Exit')
            print('1. kr-Report_2018.txt 를 읽는다.')
            print('2. Tokenization')
            print('3. Token Embedding')
            print('4. Document Embedding')
            print('5. 2018년 삼성사업계획서를 분석해서 워드클라우드를 작성하시오.')
            print('9. nltk 다운로드')
            return input('메뉴 선택 \n')

        while 1:
            menu = print_menu()
            if menu == '0':
                break
            elif menu == '1':
                self.preprocessing()
            elif menu == '2':
                self.tokenization()
            elif menu == '3':
                self.token_embedding()
            elif menu == '4':
                self.document_embedding()
            elif menu == '5':
                self.draw_wordcloud()
            elif menu == '6':
                self.read_stopword()
            elif menu == '7':
                self.remove_stopword()
            elif menu == '9':
                Solution.download()
            elif menu == '0':
                break

    @staticmethod
    def download():
        nltk.download('punkt')

    def preprocessing(self):
        self.okt.pos("삼성전자 글로벌센터 전자사업부", stem=True)
        file = self.file
        self.file.fname = 'kr-Report_2018.txt'
        path = self.new_file(file)
        with open(path, 'r', encoding='utf-8') as f:
            texts = f.read()
        texts = texts.replace('\n', ' ')
        tokenizer = re.compile(r'[^ㄱ-힣]+')
        return tokenizer.sub(' ', texts)

    def tokenization(self):
        noun_tokens = []
        tokens = word_tokenize(self.preprocessing())
        # ic(tokens[:100])
        for i in tokens:
            pos = self.okt.pos(i)
            _ = [j[0] for j in pos if j[1] == 'Noun']
            if len(''.join(_)) > 1:
                noun_tokens.append(''.join(_))
        texts = ' '.join(noun_tokens)
        ic(texts[:100])
        return texts

    def read_stopword(self):
        self.okt.pos("삼성전자 글로벌센터 전자사업부", stem=True)
        file = self.file
        self.file.fname = 'stopwords.txt'
        path = self.new_file(file)
        with open(path, 'r', encoding='utf-8') as f:
            texts = f.read()
        ic(texts)
        return texts

    def remove_stopword(self):
        tokens = self.tokenization()
        stopwords = self.read_stopword()
        texts = [i for i in tokens.split() if i not in stopwords.split()]
        # texts = [i for i in word_tokenize(tokens) if i not in word_tokenize(stopwords)] # 홍주 스타일 ><
        print(texts)

    def token_embedding(self):
        pass

    def document_embedding(self):
        pass

    def draw_wordcloud(self):
        pass

if __name__ == '__main__':
    Solution().hook()