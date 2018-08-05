class Circle:
      def __init__(self,radius):
          self.radius = radius
      def findarea(self):
          print(self.radius)
          self.area = 3.145 * self.radius**2
      def show(self):
          print(self.area)
