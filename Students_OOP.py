#school.py
class student :
    
    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname
        self.exp = 0 #คะแนนประสบการณ์
        self.lesson = 0 #จำนวนวิชาที่เคยเรียน
        self.vehicle = 'รถเมย์'    

    @property
    def fullname(self):
        return '{} {}'.format(self.name,self.lastname)

    def coding(self):
        '''นี่คือคลาสเรียนวิชาเขียนโปรแกรม'''
        self.Addexp()
        print('{} กำลังเขียนโปรแกรม...'.format(self.fullname))

    def showExp(self):
        print('{} ได้คะแนน {} exp (เรียนไป {} ครั้ง) '.format(self.name,self.exp,self.lesson))
    
    def Addexp(self):
        self.exp +=10
        self.lesson += 1

    def __str__(self):
        return self.fullname
    
    def __repr__(self):
        return self.fullname

    def __add__(self,other):
        return self.exp + other.exp

class tesla:
    def __init__(self):
        self.Model = 'รถ Tesla Model S'

    def selfDriving(self,st):
        print('ระบบขับอัตโนมัตกำลังทำงาน...กำลังพาคุณ {} กลับบ้านครับ'.format(st.name))
    
    def __str__(self):
        return self.Model

        
class specialStudent(student):

    def __init__(self,name,lastname,father):
        super().__init__(name,lastname)
        self.father= father
        self.vehicle = tesla()
        print('รู้ไหมฉันลูกใคร... ฉันเป็นลูกของ {}'.format(self.father))
    def Addexp(self):
        self.exp += 30
        self.lesson += 2
class Teacher:
    def __init__(self,fullname):
        self.fullname = fullname
        self.students = []
    def checkStudent(self):
        print('-------ลูกศิษย์ของคุณครู {}'.format(self.fullname))
        for i,st in enumerate(self.students):
            print('{} ---> {} [{} exp] [เรียนไปแล้ว {} ครั้ง ]'.format(i+1,st.fullname,st.exp,st.lesson))

    def AddStudent(self,st):
        self.students.append(st)


        
# print('FILE :',__name__)
if __name__ == "__main__":
    #day 0
    print('----DAY0----')
    allStudent = [] #ใช้สำหรับเพิ่มรายชื่อของนักเรียนไว้ใน list
    Teacher1 = Teacher('Ada lovelace')
    Teacher2= Teacher('Bill Gate')

    print(Teacher1.students)

    #day 1
    print('---DAY 1----')
    st1 = student('chanyut','maneerat')
    allStudent.append(st1)
    Teacher2.AddStudent(st1)
    print(st1.fullname)

    #day 2
    print('----DAY 2--------')
    st2 = student('stav','job')
    allStudent.append(st2)
    Teacher2.AddStudent(st2)
    print(st2.fullname)

    #day 3
    print('----DAY 3--------')
    for i in range(3):
        st1.coding()
    st2.coding()
    st1.showExp()
    st2.showExp()

    #day 4
    print('----DAY 4--------')
    stp1 = specialStudent('Tomas','Edison','Hitler')
    allStudent.append(stp1)
    stp1.fullname
    Teacher1.AddStudent(stp1)
    print('คุณครูครับ ขอคะแนนให้ผม 20 คะแนน')
    stp1.exp = 20
    stp1.coding()
    stp1.showExp()

    #day 5
    print('----DAY 5--------')
    print('นักเรียนกลับบ้านยังไงจ๊ะ')
    print(allStudent)
    for st in allStudent:
        print('ผม {} กลับบ้านด้วย {} ครับ'.format(st.name,st.vehicle))
        print(isinstance(st,specialStudent))
        if isinstance(st,specialStudent):
            st.vehicle.selfDriving(st)
    #day 6 
    print('---DAY 6----')
    Teacher1.checkStudent()
    Teacher2.checkStudent()

    print('นำคะแนนของ {} และ {} มารวมกัน ได้เท่ากับ {}'.format(st1.fullname,st2.fullname,st1 + st2))






