import random

number = random.randint(1,31)   # 1~31사이의 랜덤 integer 발생
print(f'내 마음 속 숫자: {number}')     # 발생값 표기
attempts = 0                          # 시도값 초기화

while True:                           # 루프 실행
    try:                              # input값을 int로 변환
        guess = int(input('1~31까지의 숫자 중 내가 생각한 숫자는? '))
    except ValueError:
        print('정수를 입력해야 해요!')
        continue                      # 예외 발생시 메세지 표기하여 재실행

    attempts += 1                     #유효 시도회수 셈

    print(f'입력받은 숫자: {guess}')    # 입력값 표기
    if guess > number:
        print('더 작은 숫자야!')        # 입력값이 발생값 보다 더 작은 경우
    elif guess < number:
        print('더 큰 숫자야!')          # 입력값이 발생값 보다 더 큰 경우
    else:
        print('정답!')                # 입력값과 발생값보다 크지도 작지도 않은 경우
        print(f'({attempts}번 만에 맞췄어요)') # 시도 회수 표기
        break                        # 루프 종료
