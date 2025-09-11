# 검색 -> 특정한 자료 덩어리에서 원하는 값을 찾는 것

a = [3,4,1,2,3,4,'G','F','G']
# 원하는 값의 인덱스 찾기
# 2 라는 값은 어느 위치에 있는가?
print(f'2는 어디?: {a.index(2)}')

print(f'G는 어디?: {a.index('G')}') # G는 2개 이지만 처음 찾은 값만 알려준다.

# 특정 위치부터 인덱스부터 'H'를 찾아라
print(f'G는 어디?: {a.index('G',5)}')
print(f'G는 어디?: {a.index('G',7)}')

# 값이 없으면 에러(예외)를 발생 시킨다.
# print(f'H는 어디?: {a.index('H')}')

# 리스트 요소 삭제
# del a[3]과 a.remove(3)
# del은 특정 인덱스의 값을 지운다.
# remove는 해당 값을 지운다(한개만) -> 필요시 반복해야함

# 모든 3을 찾아라
b = [3,4,1,2,3,4,5,6,1,3,2]
idx = 0                                 # idx값 초기화

# 방법1 while문(단 error 발생)            # 3값의 index를 모두 찾고자 함
# while True:                           # True 동안 실행(무한 루프)
#     idx = b.index(3,idx)              # 3값을 idx부터 찾음(초기값 0)
#     print(idx)                        # 값이 3인 idx값 출력
#     idx = idx+1                       # 같은 위치에서 반복되지 않게 값 증가

# 방법2
# for n in b:
#     if n == 3:
#         print(f'3이 있는 index {idx}')
#     idx += 1

# 위치를 리스트로 출력하기
i = []
for idx in range(len(b)):
    if b[idx] == 3:
        i.append(idx)

print(f'i: {i}')



print(f'a : {a}')
a.remove(3)
print(f'a : {a}')


# pop() = append()의 반대개념
# 맨 마지막 요소를 뺴낸다.(리스트에서 사라진다)
val = a.pop()
print(f'빼낸 값: {val} a : {a}')
val = a.pop()
print(f'빼낸 값: {val} a : {a}')

# 리스트 확장(더하기와 비슷한 개념)
print(a)
a.extend(b)
print(a)

# count(val) 특정한 값이 해당 리스트에 몇 개 있는지 확인
print(f'a안에 3이 {a.count(3)}개 있다.')
print(f'a안에 9가 {a.count(9)}개 있다.')

# a 안에 있는 모든 3을 지워주세요
# 방법 1
# for remove_count in range(a.count(3)):
#     a.remove(3)
# print(f'총 {remove_count+1}개의 3을 지운 a: {a}')

# 방법 2
idx_a = 0
while idx_a < len(a):
    if a[idx_a] == 3:
        del a[idx_a]
    idx_a += 1
print(f'3을 지운 a: {a}')