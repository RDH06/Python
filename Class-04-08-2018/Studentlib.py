class Student:
        def __init__(self,Name,Marks):
            self.Name = Name
            self.Marks = Marks
        def findavglst(self):
            avg = sum(self.Marks)/len(self.Marks)
            print(avg)
        def findavg(self):
            for walk in Marks:
                mark = walk.split(",")
            avg = sum(mark)/len(mark)
            print(avg)
        def Avglst(self):
            avg = sum(self.Marks)/len(self.Marks)
            print(avg)
        def Total(self):
            Total = sum(self.Marks)
            print(Total)
        def CompareAvg(self,obj):
            if self.Avglst != obj.Avglst:
                while self.Avglst >> obj.Avglst:
                      print(self.Avglst + "Is greater")
            else:
                 print(obj.Avglst + "Is Lesser")
                

