import csv

def readAsList():
    with open('students.csv','r',encoding='utf-8') as fp:
        reader = csv.reader(fp)
        for record in reader:
            print(record)

def readAsDict():
    with open('students.csv', 'r', encoding='utf-8') as fp:
        reader = csv.DictReader(fp)
        for record in reader:
            print(record['姓名'])

def writeAsList():
    header = ['姓名','年龄','成绩']
    students_list = [
        ('李四',8,88),
        ('王五',13,90)
    ]
    with open('students.csv','w',encoding='utf-8',newline='') as fp:
        writer = csv.writer(fp)
        writer.writerow(header)
        writer.writerows(students_list)

def writeAsDict():
    header = ['姓名','年龄','成绩']
    students_dict = [
        {'姓名':'王哈哈','年龄':12,'成绩':55},
        {'姓名':'刘白白','年龄':16,'成绩':95},
    ]
    with open('students.csv','w',encoding='utf-8',newline='') as fp:
        writer = csv.DictWriter(fp,header)
        writer.writeheader()
        writer.writerows(students_dict)


if __name__ == '__main__':
    writeAsDict()