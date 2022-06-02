import random
from hello.models import myRandom



class Quiz10:

    def quiz10bubble(self) -> str: return None

    def quiz11insertion(self) -> str: return None

    def quiz12selection(self) -> str: return None

    def quiz13quick(self) -> str: return None

    def quiz14merge(self) -> str: return None

    def quiz15magic(self) -> str: return None

    def quiz16zigzag(self) -> str: return None

    def quiz17prime(self) -> str:
        r = random.sample(range(1, 101), 2)
        r.sort()
        res = ''
        for i in range(r[0], r[1] + 1):
            count = 0
            for j in range(2, i + 1):
                if i % j == 0:
                    count += 1
            if count == 1:
                res += str(i) + ' '
        print(f'범위: {r[0]} ~ {r[1]}, 결과: {res}')
        return None

    def quiz18golf(self) -> str:
        answer = myRandom(1, 100)
        while 1:
            user = myRandom(1, 100)
            if user < answer:
                s = f'현재 숫자: {user} Up'
            elif user > answer:
                s = f'현재 숫자: {user} Down'
            elif user == answer:
                print(f'정답:{user} -> 정답 입니다.')
                return
            print(s)


    def quiz19booking(self) -> str: return None

