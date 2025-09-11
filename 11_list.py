# 파스칼표기법 - 맨 앞글자만 대문자(Java의 class 생성시 활용)
# 카멜표기법 - 단어의 의미가 있는 첫글자를 대문자로 한다(ex. shopList)
# 스네이크표기법 - 단어간의 구분을 _로 한다 (ex. shop_list)

# 리스트 생성 방법1 - 비어 있는 리스트로 생성
a = []

# 리스트 생성 방법2 - 값이 있는 리스트로 생성
shop_list = ['apple', 'mango', 'carrot', 'banana']
print(f'shop_list: {shop_list}')

# 리스트에 값을 넣는 방법
# 가장 뒤로부터 넣는 방법
a.append(1)
a.append(2)
a.append(3)
# 특정한 번호를 지정해서 넣는 방법
a.insert(1, 'X')

print(f'a의 길이: {len(a)}')
print(f'a: {a}')

# a의 2번 방에 있는 값 -> 0, 1, 2, 3
print(f'a[2]: {a[2]}')

# a의 가장 마지막 방에 있는 값
print(f'a[3]: {a[3]}')
# 길이에서 1을 뺸 값을 이용 -> 인덱스는 0번부터 시작하는 점 이용
print(f'a[last]: {len(a)-1}')
# 파이썬에서 사용되는 방식, 0보다 뒤로가면 맨 뒤로 이동된다는 개념
print(f'a[last]: {a[-1]}')

