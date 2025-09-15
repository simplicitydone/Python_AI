# 콜라, 생수, 오렌지주스, 식혜, 이온음료

# item = '콜라'
#
# if item == '콜라':
#     print(f'{item}이(가) 나왔습니다.')
# if item == '생수':
#     print(f'{item}이(가) 나왔습니다.')
# if item == '오렌지주스':
#     print(f'{item}이(가) 나왔습니다.')
# if item == '식혜':
#     print(f'{item}이(가) 나왔습니다.')
# if item == '이온음료':
#     print(f'{item}이(가) 나왔습니다.')

item = input("음료를 입력하세요: ")
items = ['콜라', '생수', '오렌지주스', '식혜', '이온음료']

if item in items:
    print(f'"{item}"이(가) 나왔습니다.')
else:
    print(f'"{item}"은(는) 보유하고 있지 않습니다.')
