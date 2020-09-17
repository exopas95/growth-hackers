'''
‘체인 소수’는 한 숫자를 연속적으로 잘라 얻을 수 있는 값들과 자기 자신이 모두 소수인 숫자를 일컫는다. 
예를 들어 ‘23’에서 얻을 수 있는 값은 ‘2’, ‘3’, ‘23’으로 ‘23’은 체인 소수로 볼 수 있다. 
이에 반해, ‘127’로 만들 수 있는 값은 ‘1’, ‘2’, ‘7’, ‘12’, ‘27’, ‘127’로 ‘127’은 체인 소수가 아니다. 
입력 받은 숫자가 체인 소수인지 판별하는 함수를 작성하라.
'''
import sys
import math

# 소수 판별 함수


def prime_number(number):
    if number < 4:
        return True
    else:
        for i in range(2, int(math.sqrt(number) + 1)):
            if (number % i) == 0:
                return False
        return True

# 입력받은 숫자를 체인으로 나누는 함수


def split_number(number):
    num_lst = list(number)
    result_lst = [int(number[0])]
    bool_lst = []

    for i in range(0, len(num_lst)):
        for j in range(2, len(num_lst)):
            if len(num_lst[i:j]) != 0:
                result_lst.append(int("".join(num_lst[i:j])))

    # 체인 숫자 소수 판별
    for num in result_lst:
        bool_lst.append(prime_number(num))

    # 결과 출력
    print(False) if False in bool_lst else print(True)


num = sys.stdin.readline()
split_number(num)
