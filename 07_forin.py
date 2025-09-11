# for문은 반복 횟수가 정해진상태에 적합하다.

# 물 10잔 떠 오기

for cup in range(10):
    print(f'물 {cup+1}번째 잔 떠왔습니다.')

# 만약 커피를 타는데 한 잔의 쿨에 믹스커피 2개씩을 넣어야 한다면?
# 반복 안에 반복이 발생된다.(반복문이 중첩된다.)
for cup in range(10):
    print(f'커피용 물 {cup+1}번째 입니다.')
    for mix in range(2):
        if mix == 0:
            print('커피믹스를 넣습니다.')
        else:
            print('커피믹스를 1개 더 추가합니다')
        for spoon in range(3):
            print(f'{spoon+1}번 젓습니다.')
print ('\n커피를 총 10잔을 만들었습니다.')