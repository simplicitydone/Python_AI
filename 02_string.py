# 문자열은 ', " 모두 사용 가능
name = 'Kim Ji-Hoon'
content = "My Content"

# 여러줄의 문자열을 담을때
multi = '''This is a multi line string.
This is the second line.'''

print('name: '+name)
print('content: '+content)
print('multi: '+multi)

#문자열에 다른 타입의 데이터를 함께 출력할 경우
age = 33

print('내 이름은 {0}이고, 나이는 {1}입니다.'.format(name, age))
print('내 이름은 '+name+'이고, 나이는 '+str(age)+'입니다.')
print(f'내 이름은 {name}이고, 나이는 {age}입니다.')

# 여러줄(다중라인) -> 한 줄 처리, 한 줄을 여러줄처럼 또는 vice versa
print('이것은 한 줄이지만,\n 여러 줄처럼 보이게 할 겁니다.') #new line
print('이것은 두 줄이지만, \
한 줄처럼 보이게 할 겁니다.')