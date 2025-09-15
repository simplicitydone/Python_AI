from jedi.inference.helpers import values_from_qualified_names

dic = {
    'name':'hong,gil-dong',
    'phone':'01012341234',
    'friends':['Alice','Smith','John']
}

# dic.keys() : 특정한 사전의 키들만 가져와 dict_keys라는 객체를 반환한다.
print(dic.keys())

for item in dic.keys():
    print(item)
keys = list(dic.keys())
print(keys)

print()
# dic.values() : 특정한 사전의 값들만 가져와 dict_values라는 객체를 반환한다.
print(dic.values())
for item in dic.values():
    print(item)
values = list(dic.values())
print(values)

print()
# dic.items() : 사전의 키:값을 한 쌍으로 가져와 dict_items로 반환한다.
# 각 키와 값은 () 모양으로 보아 tuple이다
print(dic.items())
for item in dic.items():
    print(item)
items = list(dic.items())
print(items)

print()
# 값을 가져오기 (택1)
print(dic.get('name'))
print(dic['phone'])

print()
# key: value 형태로 출력하기
# 방법1
for key, value in dic.items():
    print(f'{key}: {value}')

print()
# 방법2
for key in dic.keys():
    print(f'{key}: {dic[key]}') #또는 print(f'{key}: {dic.get(key)}')

print()
# 연습문제 : 90이상인 사람의 이름만 출력
members = {
    'kim':63, 'lee':88, 'park':97, "gang":77, "hwang":100, "ga":65,
    "na":92, "la":90, "wang":100, "gu":79
}
aScore = []
for Name, Score in members.items():
    if Score >= 90:
        aScore.append(Name)
print(f'A학점(90점 이상) 학생: {aScore}')

print()
# 검색시작 여부를 결정하는 방법 (존재여부 boolean)
yn = 'kim' in members
print(f'kim이 있는가?{yn}')

yn = 'jung' in members
print(f'jung이 있는가? {yn}')

print()
# update : 이미 있는 키면 수정을, 없는 키면 추가를 하는 함수
dic.update({'name':'홍길동", "age":30, "married":False})'})
print(dic)

print()
# dic.clear() : 사전안의 내용을 모두 지운다.
dic.clear()
print(dic)
