# 두부가게에서 두부 사오기
print('두부 가게에 간다.')

while True:
    try:
        tofubox = int(input("두부 박스 개수를 입력하세요: "))
        break  # 성공적으로 입력 받으면 반복 종료
    except ValueError:
        print("⚠️ 정수를 입력하세요.")

# 입력 받은 후 조건문 처리
if tofubox > 0:
    print('두부를 산다.')
elif tofubox == 0:
    print('순두부를 산다')
else:
    print('나한테 달라는건가?')

print('집에 온다.')