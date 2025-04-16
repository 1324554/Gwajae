# 성적 관리 프로그램
# 작성자: 홍길동
# 작성일: 2025-04-15
# 저작권: © 2025 홍길동. 무단 복제 및 배포 금지
class Student:
    def __init__(self, stu_id, name, eng, c, py):
        self.stu_id = stu_id
        self.name = name
        self.eng = eng
        self.c = c
        self.py = py
        self.sum = 0
        self.avg = 0
        self.grade = ''
        self.rank = 1
        self.calculate_scores()
        self.calculate_grade()

    def calculate_scores(self):
        self.sum = self.eng + self.c + self.py
        self.avg = self.sum / 3

    def calculate_grade(self):
        avg = self.avg
        if avg >= 95:
            self.grade = 'A+'
        elif avg >= 90:
            self.grade = 'A'
        elif avg >= 85:
            self.grade = 'B+'
        elif avg >= 80:
            self.grade = 'B'
        elif avg >= 75:
            self.grade = 'C+'
        elif avg >= 70:
            self.grade = 'C'
        elif avg >= 65:
            self.grade = 'D+'
        elif avg >= 60:
            self.grade = 'D'
        else:
            self.grade = 'F'

class StudentManager:
    def __init__(self):
        self.students = []

    def input_student(self):
        stu_id = int(input("학번: "))
        name = input("이름: ")
        eng = int(input("영어: "))
        c = int(input("C-언어: "))
        py = int(input("파이썬: "))
        self.students.append(Student(stu_id, name, eng, c, py))

    def calculate_ranks(self):
        for s1 in self.students:
            s1.rank = 1
            for s2 in self.students:
                if s2.avg > s1.avg:
                    s1.rank += 1

    def output_all(self):
        print("           성적관리 프로그램       ")
        print("===========================================================================")
        print("학번         이름       영어   C-언어  파이썬   총점   평균   학점   등수")
        print("===========================================================================")
        for s in self.students:
            print(f"{s.stu_id:<13}{s.name:<8}{s.eng:<7}{s.c:<8}{s.py:<9}{s.sum:<7}"
                  f"{s.avg:<7.2f}{s.grade:<7}{s.rank:<4}")

    def update_student(self):
        stu_id = int(input("변경할 학생의 학번: "))
        print("학번: 1, 이름: 2, 영어: 3, C언어: 4, 파이썬: 5")
        field = int(input("변경할 항목 번호: "))
        new_value = input("변경할 값: ")
        for s in self.students:
            if s.stu_id == stu_id:
                if field == 1:
                    s.stu_id = int(new_value)
                elif field == 2:
                    s.name = new_value
                elif field == 3:
                    s.eng = int(new_value)
                elif field == 4:
                    s.c = int(new_value)
                elif field == 5:
                    s.py = int(new_value)
                s.calculate_scores()
                s.calculate_grade()
        self.calculate_ranks()

    def delete_student(self):
        stu_id = int(input("삭제할 학생의 학번: "))
        self.students = [s for s in self.students if s.stu_id != stu_id]
        self.calculate_ranks()

    def find_student(self):
        query = input("찾을 사람의 이름이나 학번 입력: ")
        try:
            query = int(query)
            for s in self.students:
                if s.stu_id == query:
                    self.print_student(s)
        except ValueError:
            for s in self.students:
                if s.name == query:
                    self.print_student(s)

    def sort_students(self):
        self.students.sort(key=lambda s: s.grade, reverse=True)

    def print_student(self, s):
        print(s.stu_id, s.name, s.eng, s.c, s.py, s.sum, f"{s.avg:.2f}", s.grade, s.rank)

    def count_above_80(self):
        count = len([s for s in self.students if s.avg >= 80])
        print(f"80점 이상은 {count}명")

# 메인 실행
manager = StudentManager()
for _ in range(5):
    manager.input_student()
manager.calculate_ranks()
manager.output_all()

manager.update_student()
manager.delete_student()
manager.find_student()
manager.sort_students()
manager.output_all()
manager.count_above_80()
