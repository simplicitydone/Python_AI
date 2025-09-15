class Puppy:    			 	# 클래스 생성

    name = ""                   # 멤버, 변수(필드) : class 안에서 사용 가능한 변수
    goal = ""                   # 클래스 변수 (name, goal은 instance 생성시 덮어씌워짐)
    species = "달마시안"

    def __init__(self, name, goal): # 생성자 : 객체화시 호출되는 함수다)
        # 받아온 name과 goal은 이 생성자를 벗어날 수 없다. (생성자의 쓰임이 다하면 함께 없어진
        # 그래서 클래스(객체) 멤버에 넣어줘야, 객체가 살아있는 동안 사용이 가능하다
        # 그런데 name = name 형태로는 어떤것이 객체의 멤버인지 알 수 없다.
        # 그래서 멤버인 녀석은 self를 이용하여 표시해 준다.
        self.name = name        # name과 goal은 객체 변수이며, 받아온 값(속성)으로 초기화
        self.goal = goal        #self.을 하지 않으면 객체에 저장되지 않음



puppy = Puppy("멍멍이", "집지키기")
print(puppy.name)
print(puppy.goal)
print(puppy.species)



