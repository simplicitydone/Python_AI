# 3값의 index를 모두 찾고자 함

b = [3,4,1,2,3,4,5,6,1,3,2]
idx = 0                               # idx값 list 처음값으로 초기화

while True:                           # True 동안 실행(무한 루프)
    idx = b.index(3,idx)       # 3값을 idx부터 찾음(초기값 0)
    print(idx)                        # 값이 3인 idx값 출력
    idx = idx+1                       # 같은 위치에서 반복되지 않게 값 증가
