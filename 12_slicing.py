# 슬라이싱(특정 영역만큼 선택해서 보여주거나 값을 추가하는 방법)

arr = ['Life', 'is', 'too', 'short']
# arr[보여주기 시작하는 인텍스:버릴 인덱스]
area = arr[0:2] # 0번부터 보여주고 2번부터 버린다
print(area)
area = arr[2:4]
print(area)
area = arr[:2] # 0번부터 보여준다
print(area)
area = arr[2:] # -1번(마지막)까지 보여준다
print(area)

# 특정 영역을 지정해서 값을 추가 할 수도 있다.
arr[1:3] = ['a', 'b', 'c'] # 1-2 영역을 a,b,c로 대체하겠다.
print(arr)
arr[2:3] = ['가', '나', '다'] # 2-3 영역을 가나다로 대체하겠다.
print(arr)
arr[2:2] = ['가', '나', '다'] # 2영역 다음에 가나다를 넣음.
print(arr)

#[Life, A, B, C, short]
arr[1:9] = ['A', 'B', 'C'] # 2-3 영역을 a,b,c로 대체하겠다.
print(arr)

# 리스트끼리 연산
a = [1,2,3,4,5]
b = ['a','b','c','d']
print(a+b)
print(a*3)