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

# 모든 3을 찾아라
b = [3,4,1,2,3,4,5,6,1,3,2]
idx = 0

# 방법1 while문(단 error 발생
# while True:
#     idx = b.index(3,idx)
#     print(idx)
#     idx = idx+1

# 방법2
for n in b:
    if n == 3:
        print(f'3이 있는 index {idx}')
    idx += 1

#
# i = []
# for n in range(len(b)):
#     j = [b.index(3)]
#     i = i + j
#
# print(f'i: {i}')
#
#
#
#
#
