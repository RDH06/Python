
          class Student:
        def __init__(self,Name,Marks):
            self.Name = Name
            self.Marks = Marks
        def findavglst(self):
            avg = sum(self.Marks)/len(self.Marks)
            print(avg)
        def findavg(self):
            Mark = self.Marks(",")    
            Mark = [int(r) for r in Mark]
            avg = sum(Mark)/len(Mark)
            print(avg)
        def Avglst(self):
            avg = sum(self.Marks)/len(self.Marks)
            print(avg)
        def Total(self):
            Total = sum(self.Marks)
            print(Total)
        def CompareAvg(self,obj):
            S1=self.findavglst()
            S2=obj.findavglst()
            print ("S1",S1,"S2",S2)
            if S1 > S2:
                print((S1-S2)+ "S1 is Greater")
            elif S2 > S1:
                 print((S2-S1)+ "S2 is Greater")      

