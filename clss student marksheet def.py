class Student:
    TotalStudent=0
    def __init__(obj,Rno=0,Name='-',Course='-'):
        obj.Rno=Rno
        obj.Name=Name;
        obj.Course=Course
        Student.TotalStudent+=1;
        return
    def input(obj):
        obj.Rno=int(input('Enter Roll No :'))
        obj.Name=input('Enter Name :')
        obj.Course=input('Enter Course :')
        return
    def output(obj):
        print('Roll No     :',obj.Rno)
        print('Name        :',obj.Name)
        print('Course      :',obj.Course)
        return
    def showTotalStudent(obj):
        print('Total Student :',Student.TotalStudent)
        return

class Result(Student):
    def __init__(obj,P=0,C=0,M=0):
        obj.P=P
        obj.C=C
        obj.M=M
        return
    def input(obj):
        obj.P=int(input('Enter Marks of Physics    :'))
        obj.C=int(input('Enter Marks of Chemistry  :'))
        obj.M=int(input('Enter Marks of Math       :'))
        return
    def output(obj):
        print('Marks of Physics   :',obj.P)
        print('Marks of Chemistry :',obj.C)
        print('Marks of Math      :',obj.M)
        return
                 

R=Result()
R.input()
R.output()
                      
                      
