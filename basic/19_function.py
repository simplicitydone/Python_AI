# 함수선언(define)
def toaster(bread):
    #pass # 오류가 나도 통과(오류가 발생하지 않도록 하는 함수)
    print(f'{bread}이 구워지고 있다.')
    return f'구워진 {bread}'

dish = toaster('세상에서 가장 맛있는 식빵')
print(dish)
