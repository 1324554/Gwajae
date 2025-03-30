StuID = []
StuName = []
EngScore = []
CScore = []
PyScore = []
SumScore = []
AvgScore = []
StuGrade = []
StuRank = [1, 1, 1, 1, 1]

def DataInput():
    StuID.append(int(input('학번: ')))
    StuName.append(input('이름: '))
    EngScore.append(int(input('영어: ')))
    CScore.append(int(input('C-언어: ')))
    PyScore.append(int(input('파이썬: ')))

def ScoreCalc(num):
    SumScore.append(EngScore[num] + CScore[num] + PyScore[num])
    AvgScore.append(SumScore[num] / 3)

def GradeCalc(num):
        if AvgScore[num] >= 95:
            StuGrade.append('A+')
        elif AvgScore[num] >= 90:
            StuGrade.append('A')
        elif AvgScore[num] >= 85:
            StuGrade.append('B+')
        elif AvgScore[num] >= 80:
            StuGrade.append('B')
        elif AvgScore[num] >= 75:
            StuGrade.append('C+')
        elif AvgScore[num] >= 70:
            StuGrade.append('C')
        elif AvgScore[num] >= 65:
            StuGrade.append('D+')
        elif AvgScore[num] >= 60:
            StuGrade.append('D')
        else:
            StuGrade.append('F')

def RankCalc():
    num = len(StuID)
    for i in range(num):
        for j in range(num):
            if AvgScore[j] > AvgScore[i]:
                StuRank[i] += 1

def DataOutput():
    print('           성적관리 프로그램       ')
    print('=========================================================================')
    print('학번         이름       영어   C-언어  파이썬   총점   평균   학점   등수')
    print('=========================================================================')
    
    for i in range(5):
        print(f'{StuID[i]:<13}{StuName[i]:<8}{EngScore[i]:<7}{CScore[i]:<8}{PyScore[i]:<9}'
              f'{SumScore[i]:<7}{AvgScore[i]:<7.2f}{StuGrade[i]:<7}{StuRank[i]:<4}')
        
def Insertion():
    num = len(StuID)
    changer = int(input("변경할 학생의 학번"))
    print('학번: 1, 이름: 2, 영어: 3, C언어: 4, 파이썬: 5')
    changes = int(input('변경할 값의 종류'))
    if changes != 2:
        val = int(input('변경할 값'))
    else:
        val = input('변경할 값')
    for i in range(num):
        if StuID[i] == changer:
            if changes == 1:
                StuID[i] = val
            elif changes == 2:
                StuName[i] = val
            elif changes == 3:
                EngScore[i] = val
            elif changes == 4:
                CScore[i] = val
            else:
                PyScore[i] = val
        ScoreCalc(i)
        GradeCalc(i)
        RankCalc()
    
def Deletion():
    num = len(StuID)
    deleted = int(input('삭제할 사람의 학번'))
    for i in range(num):
        if StuID[i] == deleted:
            del StuID[i], StuName[i], EngScore[i], CScore[i], PyScore[i], SumScore[i], AvgScore[i], StuGrade[i], StuRank[i]
            ScoreCalc(i)
            GradeCalc(i)
            RankCalc()

def Find():
    num = len(StuID)
    isName = False
    finder = input('찾을 사람의 이름이나 학번 입력')
    try:
        finder = int(finder)
    except:
        isName = True
    if isName:
        for i in range(num):
            if StuName[i] == finder:
                print(StuID[i], StuName[i], EngScore[i], CScore[i], PyScore[i], SumScore[i], AvgScore[i], StuGrade[i], StuRank[i], sep=' ')
    else:
        for i in range(num):
            if StuID[i] == finder:
                print(StuID[i], StuName[i], EngScore[i], CScore[i], PyScore[i], SumScore[i], AvgScore[i], StuGrade[i], StuRank[i], sep=' ')

def Sort():
    sorted_data = sorted(zip(StuGrade, StuID, StuName, EngScore, CScore, PyScore, SumScore, AvgScore, StuRank), reverse=True)
    global StuGrade, StuID, StuName, EngScore, CScore, PyScore, SumScore, AvgScore, StuRank
    StuGrade, StuID, StuName, EngScore, CScore, PyScore, SumScore, AvgScore, StuRank = map(list, zip(*sorted_data))

def AboveB():
    num = len(StuID)
    count = 0
    for i in range(num):
        if AvgScore[i] >= 80:
            count += 1
    print(f'80점 이상은 {count}명')

for i in range(5):
    DataInput()
    ScoreCalc(i)
    GradeCalc(i)
    RankCalc()
DataOutput()
Insertion()
Deletion()
Find()
Sort()
AboveB()
