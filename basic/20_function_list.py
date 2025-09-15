# 반환타입: O 매개변수: O  -->  자판기
def vender(can):
    print(f'{can}을 선택하셨습니다.')
    return f'{can}가 나왔습니다.'

a = vender('콜라')             # 매개변수 있음
print(a)                      # 반환값 있음


# 반환타입: O 매개변수: X  -->  번호표
def num_print():
    return '번호표가 나왔습니다.'

a = num_print()             # 매개변수 없음
print(a)                    # 반환값 있음


# 반환타입: X 매개변수: O  -->  저금통
def piggy(coin):
    print(f'{coin}을 넣었습니다')

a = piggy('100원')           # 매개변수 있음
print(a)                     # 반환값 없음


# 반환타입: X 매개변수: X  -->  호출벨
def call_bell():
    print('벨이 울립니다.')

a = call_bell()             # 매개변수 없음
print(a)                    # 반환값 없음