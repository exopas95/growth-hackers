"""
신입생이 학교에 입학할 때 부여되는 ‘학번’은 일정한 규칙을 가지고 만들어진다. 
학번은 가령 ‘2020-12345’의 형태와 같이 총 9자리의 숫자로 구성되는데, 처음 네 자리는 입학년도로 설정된다. 
그 다음 숫자는 학부/석사/박사의 경우 각각 1/2/3이 부여되며, 마지막 네 자리는 랜덤한 값으로 정해진다. 
이 때, 새로운 학생이 입학할 때마다 딕셔너리에 학번을 키(key), 학생의 이름을 밸류(value)로 저장하는 함수를 만들고자 한다. 
위 규칙에 따라 ‘입학년도’, ‘학부/석사/박사 여부’, ‘이름’을 입력받고 학번을 생성하여 이를 딕셔너리에 학번을 키(key), 이름을 밸류(value)로 저장하는 함수를 작성하라. 
(단, 중복되는 학번이 만들어져서는 안 된다.)
"""
import sys
import random

# 학번 생성 함수


def info_constructor(information, stu_dict):
    year = information[0]                               # 년 정보
    graduate = 0                                        # 학사/석사/박사 번호 변수 초기화
    if information[1] == '학부':
        graduate = 1                                    # 학사인 경우 1번
    elif information[1] == '석사':
        graduate = 2                                    # 석사인 경우 2번
    else:
        graduate = 3                                    # 박사인 경우 3번

    # 중복 학번 방지
    while True:
        num = random.randrange(0, 10000)             # 마지막 랜덤한 네 자리 숫자 생성
        if num < 10:
            num = "000" + str(num)
        elif num < 100:
            num = "00" + str(num)
        elif num < 1000:
            num = "0" + str(num)
        else:
            num = str(num)

        stu_num = year + "-" + str(graduate) + num  # 학번 생성

        # 생성한 학번이 딕셔너리에 이미 있는지 확인
        if stu_num not in stu_dict:
            stu_dict[stu_num] = information[2]          # 입력한 학번 딕셔너리에 저장
            return stu_dict                             # 딕셔너리 반환
        else:
            print("중복된 학번입니다.")
            continue                                    # 중복된 경우 random 함수 반복 실행


info_dict = {}                                          # 학생 정보 딕셔너리

while True:
    info = sys.stdin.readline().strip()                 # 입력 값 받기
    if info == "":                                      # Loob 끝내기 위해 조건문 추가
        break
    else:
        info_lst = info.split(',')                      # 입력 값 리스트로 변환하기
        result = info_constructor(info_lst, info_dict)  # 추가한 학번 딕셔너리에 저장해서 반환
        print(result)                                   # 결과 출력
