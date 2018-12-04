__author__ = 'Канцеров Александр'

import sys
import math

  class Triangle:
	  def __init__(self, point1, point2, point3):
      self.x1 = float(point1[0])
		  self.y1 = float(point1[1])
		  self.x2 = float(point2[0])
		  self.y2 = float(point2[1])
		  self.x3 = float(point3[0])
		  self.y3 = float(point3[1])
    
	  def get_area(self):
      area = math.fabs(self.x1*(self.y2-self.y3) + self.x2*(self.y3-self.y1) + self.x3*(self.y1-self.y2)) / 2.0
      return area
	  
    def get_perimeter(self):
      self.a = math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
      self.b = math.sqrt((self.x3-self.x1)**2+(self.y3-self.y1)**2)
      self.c = math.sqrt((self.x3-self.x2)**2+(self.y3-self.y2)**2)
      return self.a + self.b + self.c
    
    def get_heights(self):
      height_a = 2*self.get_area() / self.a
      height_b = 2*self.get_area() / self.b
      height_c = 2*self.get_area() / self.c
      return [height_a, height_b, height_c]
