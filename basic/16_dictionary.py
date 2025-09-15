# Dictionary는 Key와 value로 구성되며, key는 중복될 수 없다 (중복 될 경우 덮어쓴다)
# 비슷한 자료구조로는 자바스크립트에 오브젝트, 자바의 맵이 있다.

dic1 = {
    'name':'kim,ji-hoon',
    'phone':'01012341234',
    'age':55
}

dic2 = {
    'name':'hong,gil-dong',
    'phone':'01022335454',
    'friends':['Alice', 'John', 'Smith']
}

# 사전에 데이터 넣기 1
a = {'first':'a'}
print(a)

# 사전에 데이터 넣기 2
a['second'] = 'b'
print(a)

# 사전에서 특정 요소 삭제
del a['second']
print(a)

# 사전에 특정 요소를 꺼내보자
print(dic2['name'])
print(dic2['friends'])          # 값이 없을 경우 error 발생
# get 함수 이용시 에러 대신에 반환값(None 또는 기본값)이 있도록 할 수 있음
print(dic2.get('phone'))
print(dic2.get('nick','해당 내용이 없음')) # None 대체 내용으로 반환