class Parent():
    def __init__(self):
        print("부모 생성자 실행!")

class Child(Parent):
    def __init__(self):
        super().__init__() # 생략된 부모 생성자
        print("자식 생성자 실행!")

ch = Child() # 부모 생성자 -> 자식 생성자 순으로 실행


# 부모가 초기화가 필요하다면 자식에게 값을 전달해서 자식이 부모에게 전달하도록 한다.
class SchoolMember:
    name = ""
    age = 0

    def __init__(self, name, age): # 3. 받아온 값으로 초기와 하고 객체화 된다.
        self.name = name
        self.age = age

class Teacher(SchoolMember):
    salary = 0

    def __init__(self, name, age, salary):
        super().__init__(name, age) # 2. 부모를 먼저 객체화 시키면서 초기화 할 값을 전달
        self.salary = salary # 4. 그리고 나서 내가 초기화 하면서 객체화 한다.

# 1. Teacher라는 클래스를 객체화 한다. (초기화를 위해 매개변수를 전달)
t = Teacher("김철수", 33, 5000000)
# 5. name과 age는 부모 것이지만 내 것 처럼 내 객체에서 가져다 쓸 수 있게 된다.
print(f'{t.name}, {t.age},- {t.salary}')


