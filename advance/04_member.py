class Robot:    # 기본 생성자 -> 객체화 요청

    # 생성자 : 객체화 할 때 호출되는 함수의 일종으로
    # 객체화가 될 때 가장 먼저 호출된
    def __init__(self):
        print('Robot이 복사될때 제일 먼저 호출되는 멤버')


    def doIt(self):
        print("나는 Robot의 함수입니다.")

robot = Robot()
robot.doIt()
