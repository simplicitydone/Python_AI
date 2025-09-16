class Runner:
    def run(self):
        print("달린다.")
    def sprint(self):
        print("전력질주를 한다.")

class Jumper:
    def jump(self):
        print("점프를 한다")

    def high_jump(self):
        print("높이 점프를 한다.")

class Person(Jumper, Runner): # Jumper와 Runner를 상속 받았다.
    def walk(self):
        print("걷는다.")


# walk() 함수를 사용하기 위해 Person 클래스를 객체화 한다.
p = Person()
p.walk()
p.sprint()
p.high_jump()
