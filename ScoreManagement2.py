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
    for i in range(5):
        for j in range(5):
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

for i in range(5):
    DataInput()
    ScoreCalc(i)
    GradeCalc(i)
RankCalc()
DataOutput()
