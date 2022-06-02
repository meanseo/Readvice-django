import random

from hello.domains import Member
from hello.domains import my100, myRandom, members


class Quiz00:
    def quiz00calculator(self) -> float:
        a = my100()
        b = my100()
        op = ['+', '-', '*', '/', '%']
        res = op[myRandom(0, len(op) - 1)]
        if res == '+':
            s = self.add(a, b)
        elif res == '-':
            s = self.sub(a, b)
        elif res == '*':
            s = self.mul(a, b)
        elif res == '/':
            s = self.div(a, b)
        elif res == '%':
            s = self.mod(a, b)
        print(f'{a} {res} {b} = {s}')
        return None

    def add(self, a, b) -> float:
        return a + b

    def sub(self, a, b) -> float:
        return a - b

    def mul(self, a, b) -> float:
        return a * b

    def div(self, a, b) -> float:
        return a / b

    def mod(self, a, b) -> float:
        return a % b

    def quiz01bmi(self):
        this = Member()
        this.name = members()[myRandom(0,len(members())-1)]
        this.height = myRandom(1, 200)
        this.weight = myRandom(1, 200)
        res = this.weight / (this.height * this.height) * 10000
        if res > 30:
            s = f'고도 비만'
        elif res > 25:
            s = f'비만'
        elif res > 23:
            s = f'과체중'
        elif res > 18.5:
            s = f'정상'
        else:
            s = f'저체중'
        print(f'{this.name}님, {s} 입니다.')
        return None

    @staticmethod
    def quiz02dice():
        return myRandom(1, 6)

    def quiz03rps(self):
        c = myRandom(1, 3)
        p = input('가위', '바위', '보')
        # 1 가위 2  바위 3 보
        rps = ['가위', '바위', '보']
        if p == c:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:무승부'
        elif p - c == 1 or p - c == -2:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:승리'
        elif p - c == -1 or p - c == 2:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:패배'
        else:
            res = '1~3 입력'
        print(res)

    def quiz04leap(self):
        year = myRandom(2000, 2050)
        '''
        java style
        s = (year % 4 == 0 and year % 100 != 0) ? "윤년" : (year % 400 == 0) ? "윤년" : "평년"
        '''
        print(f'{year}년은 윤년' if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else f'{year}년은 평년')
        return None

    def quiz05grade(self):
        name = members()[myRandom(0,23)]
        kor = myRandom(0, 100)
        eng = myRandom(0, 100)
        math = myRandom(0, 100)
        sum = self.sum(kor, eng, math)
        avg = self.avg(kor, eng, math)
        grade = self.grade(kor, eng, math)
        passChk = self.passChk(kor, eng, math)

        print(f'{name}님, 국어 점수 : {kor} \n '\
                  f'영어 점수 : {eng}\n 수학 점수: {math}\n'\
                  f'총합: {sum} 평균: {avg} 등급: {grade} 합격 여부: {passChk}')
        return None

    def sum(self, kor, eng, math):
        return kor + eng + math

    def avg(self, kor, eng, math):
        return self.sum(kor, eng, math) / 3

    def passChk(self, kor, eng, math):  # 60점 이상 이면 합격
        return '합격' if self.avg(kor, eng, math) >= 60 else '불합격'

    def grade(self, kor, eng, math):
        if (self.avg(kor, eng, math)) >= 90:
            return 'A등급'
        elif (self.avg(kor, eng, math)) >= 70:
            return 'B등급'
        elif (self.avg(kor, eng, math)) >= 60:
            return 'C등급'
        elif (self.avg(kor, eng, math)) >= 40:
            return 'D등급'
        else:
            return 'F등급'

    @staticmethod
    def quiz06member_choice():
        return members()[myRandom(0, 24)]

    @staticmethod
    def quiz07lotto():
        a = random.sample(range(1, 47), 6)
        a.sort()
        print(a)
        return a

    def quiz08bank(self):  # 이름, 입금, 출금만 구현
        '''total = 0
        money = myRandom(0, 100000)

        while 1:
            bankMenu = int(input('0.Exit 1.입금 2.출금 3.잔고 확인'))
            if bankMenu == 0:
                return
            elif bankMenu == 1:
                s = self.add(total, money)
                total += s
            elif bankMenu == 2:
                s = self.sub(total, money)
                total -= s
            elif bankMenu == 3:
                s = total
            else:
                s = '잘못된 번호 입니다.'
            print(s)'''

        print('------------------------------')
        Account.main()

    def save(self, total, money):
        return total + money

    def pay(self, total, money):
        return total - money

    @staticmethod
    def quiz09gugudan():  # 책받침 구구단
        for i in range(2, 10, 4):
            for j in range(1, 10):
                for k in range(i, i + 4):
                    print(f'{k} * {j} = {k * j}\t', end='')
                print('\n', end='')
            print('\n', end='')
            return None


'''
은행 이름은 비트 은행
입금자 이름(name), 계좌번호(account_number), 금액(money) 속성 값으로 계좌를 생성한다. --> 속성 값을 설정하는 것이 첫번째
계좌 번호는 3자리-2자리-6자리 형태로 랜덤하게 생성된다.
예를 들면 123-12-123456 이다.
금액은 100 ~ 999 사이로 랜덤하게 입금된다. (단위는 만 단위로 암묵적으로 판단한다.)
'''
class Account(object):
    def __init__(self, name, account_number, money):
        self.BANK_NAME = '비트 은행'
        self.name = members()[myRandom(0, 23)] if name == None else name
        self.money = myRandom(100, 999) if money == None else money
        # self.account_number = f'{myRandom(0, 1000):0>3} - {myRandom(0, 100):0>2} - {myRandom(0, 1000000):0>6}'
        self.account_number = self.create_account_number() if account_number == None else account_number

    def to_string(self):
        return f'은행 : {self.BANK_NAME} ' \
               f'입금자 : {self.name} 님 ' \
               f'계좌 번호 : {self.account_number} ' \
               f'금액: {self.money}만원'

    def create_account_number(self):
        '''
        ls = [str(myRandom(0, 10)) for i in range(3)]
        ls.append("-")
        ls += [str(myRandom(0, 10)) for i in range(2)]
        ls.append("-")
        ls += [str(myRandom(0, 10)) for i in range(6)]
        return "".join(ls)
        '''

        return ''.join(['-' if i == 3 or i == 6 else str(myRandom(0, 10)) for i in range(13)])
        # return ''.join([str(myRandom(0, 10)) if i != 3 and i != 6 else '-' for i in range(13)])

    @staticmethod
    def find_account(ls, account_number):
        # return ''.join(j.to_string() if j.account_number == account_number else '찾는 계좌 아님' for i, j in enumerate(ls))
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                return ls[i]

    @staticmethod
    def deposit(ls, account_number, deposit):
        m = Account.find_account(ls, account_number)
        m.money += deposit
        return m

    @staticmethod
    def withdrawal(ls, account_number, withdrawal):
        m = Account.find_account(ls, account_number)
        m.money -= withdrawal
        return m

    @staticmethod
    def del_account(ls, account_number):
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                del ls[i]


    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0.종료 1.계좌개설 2.계좌내용 3.입금 4.출금 5.계좌해지 6.계좌조회')
            if menu == '0':
                break
            if menu == '1':
                a = Account(None, None, None)
                print(f'{a.to_string()} ... 개설되었습니다.')
                ls.append(a)
            elif menu == '2':
                r = '\n'.join([i.to_string() for i in ls])
                print(r)
            elif menu == '3':
                r = Account.deposit(ls, input('입금할 계좌번호'), int(input('입금액')))
                print(r.to_string)
                break
            elif menu == '4':
                r = Account.withdrawal(ls, input('출금할 계좌번호'), int(input('출금액')))
                print(r.to_string)
                break
            elif menu == '5':
                Account.del_account(ls, input('해지할 계좌번호'))
                break
            elif menu == '6':
                r = Account.find_account(ls, input('조회할 계좌번호'))
                print(r.to_string())
                break
            else:
                print('Wrong Number.. Try Again')
                continue



