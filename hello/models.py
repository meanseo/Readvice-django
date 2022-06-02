import random

class Quiz01Calculator(object):

    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2

    def calc(self):
        if self.op == '+':
            s = self.add()
        elif self.op == '-':
            s = self.sub()
        elif self.op == '*':
            s = self.mul()
        elif self.op == '/':
            s = self.div()
        return s

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

class Quiz02Bmi(object):
    @staticmethod
    def bmi(member):
        this = member
        bmi = this.weight / (this.height * this.height) * 10000
        if bmi > 30:
            res = '고도 비만 입니다.'
        elif bmi > 25:
            res = '경도 비만 입니다.'
        elif bmi > 23:
            res = '과체중 입니다.'
        elif bmi > 18.5:
            res = '정상 체중 입니다.'
        else:
            res = '저체중 입니다.'
        return res

class Quiz03Grade(object):

    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def getGrade(self):
        return f'이름 : {self.name} \n 국어 점수 : {self.kor} \n '\
                  f'영어 점수 : {self.eng}\n 수학 점수: {self.math}\n'\
                  f'총합: {self.total()} 평균: {self.avg()} 합격 여부: {self.chkPass()}'

    def total(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return (self.kor + self.eng + self.math) / 3

    def chkPass(self):
        return '합격' if self.avg() >= 60 else '불합격'

class Quiz04GradeAuto(object):

    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return (self.kor + self.eng + self.math) / 3

    def getGrade(self):
        pass

    def chkPass(self):
        pass

def myRandom(start, end):
    return random.randint(start, end)

class Quiz05dice(object):
    @staticmethod
    def getDice():
            return myRandom(1, 6)

class Quiz07RandomChoice(object):
    def __init__(self):
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        '권혜민', '서성민', '조현국', '김한슬', '김진영',
                        '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        '강 민', '최건일', '유재혁', '김아름', '장원종']

    def chooseMember(self):
        ran = myRandom(0, len(self.members)-1)
        return self.members[ran]
        # res = random.choice(self.members)

class Quiz08Rps(object):
    def __init__(self,user):
        self.user = user
        self.com = myRandom(1, 3)

    def game(self):
        p = self.user
        c = self.com
        # 1 가위 2 바위 3보자기
        rps = ['가위', '바위', '보']
        if p == c:
            res = f'플레이어:{rps[p-1]}, 컴퓨터:{rps[c-1]}, 결과:무승부'
        elif p-c == 1 or p-c == -2:
            res = f'플레이어:{rps[p-1]}, 컴퓨터:{rps[c-1]}, 결과:승리'
        elif p-c == -1 or p-c == 2:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:패배'
        else:
            res = '잘못된 번호 입니다.'
        return res

class Quiz09GetPrime(object):

    def getPrime(self):
        start = int(input('start 수를 입력하세요.'))
        end = int(input('end 수를 입력하세요.'))
        for i in range(start, end+1):
            count = 0
            for j in range(2, i+1):
                if i % j == 0:
                    count += 1
            if count == 1:
                print(i)

class Quiz10LeapYear(object):
    def __init__(self, year):
        self.year = year

    def getLeapYear(self):
        return '윤년' if ((self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0) else '평년'

class Quiz11NumberGolf(object):
    @staticmethod
    def numGame():
        answer = myRandom(1, 100)
        while 1:
            user = int(input('값을 입력하세요.'))
            if user < answer:
                print('Up')
            elif user > answer:
                print('Down')
            else:
                return '정답 입니다.'


class Quiz12Lotto(object):
    @staticmethod
    def lotto():
        a = random.sample(range(1, 46), 6)
        a.sort()
        return a

class Quiz13Bank(object): # 이름, 입금, 출금만 구현
    def __init__(self, name):
        self.name = name
        self.money = 0

    def bank(self):
        while 1:
            bankMenu = int(input('0.Exit 1.입금 2.출금 3.잔고 확인'))
            if bankMenu == 0:
                return
            elif bankMenu == 1:
                return self.add()
            elif bankMenu == 2:
                return self.sub()
            elif bankMenu == 3:
                return self.total()
            else:
                print('잘못된 번호 입니다.')

    def add(self):
        self.money += int(input('입금 금액: '))

    def sub(self):
        self.money -= int(input('출금 금액: '))

    def total(self):
        print( f'{self.name} 님의 잔고: {self.money} 원 입니다.')



class Quiz14Gugudan(object): # 책받침 구구단
    @staticmethod
    def gugudan():
        for i in range(2, 10, 4):
            for j in range(1, 10):
                for k in range(i, i+4):
                    print(f'{k} * {j} = {k*j}\t', end='')
                print('\n', end='')
            print('\n', end='')