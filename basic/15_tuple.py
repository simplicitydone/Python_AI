tu1 = (1,2,3) #tuple은 []가 아닌 ()로 선언
tu2 = ('a','b','c')
tu3 = (1, 2, ('a', 'b'))

a = [1, 2, 3]
tu4 = (1, 2, a)

print(tu4)
a = a.append(4)
print(tu4)

# 불러오기
print(tu1[1])
# slicing
print(tu2[1:])
# 더하기
print(tu1+tu2)
# 곱하기
print(tu1*3)

#tuple과 리스트간의 상호전환
tu2list = list(tu2)
print(f'{tu2} -> {tu2list}')
list2tu = tuple(tu2list)
print(f'{tu2list} -> {list2tu}')