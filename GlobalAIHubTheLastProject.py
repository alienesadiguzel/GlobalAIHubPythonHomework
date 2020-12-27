#sabit bir kullanıcı yok, önce kayıt olmanız lazım.

class studentManSys:
    def __init__(self,name=[], lesson=[]):
        self.name=name
        self.lesson=lesson
        self.program=True
        self.eLesson= []
        self.lessonList=["Math".upper(),"Physics".upper(),"Chemistry".upper(),"Statics".upper(),"Thermodynamics".upper(),"Machine Elements".upper()]
        self.grades={}

    def menu(self):
        print("""----------- Welcome our Student Management System -----------\n 1-Login\n 2-Sign Up\n """)
    def menuChoose(self):
        choose=int(input("Plz enter your choose: "))
        return choose

    def addLesson(self):
        print("The courses we can choose are on the list:\n {}".format(self.lessonList))
        self.selectLesson=int(input("""Please enter the number of courses you want to choose.\nThis selection should be between 3 and 5: """))
        if self.selectLesson < 3 and self.selectLesson > 5:
            print("You failed in class!")
        else:
            for s in range (1,self.selectLesson+1):
                enterLesson=input("Plz enter the course you want: ")
                if enterLesson.upper() in self.lessonList:
                    self.lesson.append(enterLesson)
                    print("Your Choices are {}".format(self.lesson))
                else:
                    print("You cant select that lesson!")
                    self.lesson.clear()
                    self.addLesson()
    def selectExam(self):
        print("Your choices are {}".format(self.lesson))
        examLesson=input("Please enter the course take exam your want: ")
        if examLesson in self.lesson:
            midterm=int(input("Plz your midterm grade:"))
            self.grades["midterm"]=midterm
            final=int(input("Plz your final grade:"))
            self.grades["final"] = final
            project=int(input("Plz your project grade:"))
            self.grades["project"] = project
            print(self.grades)
            avarage= (midterm*(30/100) + final*(50/100) + project*(20/100))
            if avarage >= 90:
                print("Congratulations! Your Grade is AA")
            elif 70<=avarage<90:
                print("Your Grade is BB")
            elif 50<=avarage<70:
                print("Your Grade is CC")
            elif 30<=avarage<50:
                print("Your Grade is DD")
            elif avarage<30:
                print("You failed in class :(")


    def running(self):
        self.menu()
        select=self.menuChoose()
        counter=0
        if select ==1:
            while self.program:
                whats_urname=input("Plz Enter Your Name: ")
                if whats_urname.upper() not in self.name:
                        print("Your name is wrong! Plz enter true name!: ")
                        counter+=1
                        if counter==3:
                            print("Please Try Again Later")
                            self.program=False
                else:
                    self.addLesson()
                    self.selectExam()
                    self.running()
        if select==2:
            loginName=input("Plz enter your name and surname for sign up!: ")
            self.name.append(loginName.upper())
            print("Congratulations! You are in!")


student=studentManSys()

while student.program:
    student.running()






