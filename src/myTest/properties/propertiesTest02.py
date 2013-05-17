"""
Created on 2013-5-16

@author: lavenda
"""

from myTest.properties.propertiesTest import Square


class SubSquare(Square):
    def __init__(self, side):
        Square.__init__(self, side)
    
    def __getPerimeter(self):
        return self.side * 5
    
    def __setPerimeter(self, perimeter):
        Square.__setPerimeter(self, perimeter)
    
    perimeter = property(__getPerimeter, __setPerimeter,
                         doc = """aaa""")
    
if __name__ == '__main__':
    ssq = SubSquare(3)
    ssq2 = SubSquare(3)
    print ssq.perimeter
    print ssq2.perimeter
    ssq.side = 5
    print ssq.perimeter
    print ssq2.perimeter