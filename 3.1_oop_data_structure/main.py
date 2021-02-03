# coding=utf-8
# This is a sample Python script.
from classes import Shape, Point, Polygon, Circle, Square, Rectangle, Segment, Triangle
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import unittest,re, inspect

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def test_case(self):
    """test Circle.__contains__"""
    ans = "\n" + inspect.stack()[0][3] + ": \n"
    for i in range(3):
        s1 = Shape()
        ans += str(s1) + "\n"
        ans += s1.details() + "\n"

    self.check(ans, 4169, True)

class TestShapeMethod(unittest.TestCase):

    def check (self, string_output, ansKey, trace  = True):
        s= string_output
        s = re.sub("\s", "", s)
        s = re.sub("\(id=\d+\)", "", s)

        a= sum ( [ ord(x) for x in s ]) # encoding
        if trace:
            print (string_output)
        msg = inspect.stack()[1][3] + ": "
        if (a == ansKey):
            msg += "pass!"
        else:
            msg +=  "fail!"
            print (a, ansKey)
        print (msg)
        return None

TestShapeMethod.test_case = test_case
unittest.main(argv=[''], verbosity=0, exit=False)

TestShapeMethod.test_Circle_contains = None

s = """
Expected outputs (except the id numbers and the spaces could be different


test_case: 
Shape(id=0)
Shape(id=0):         
Shape(id=1)
Shape(id=1):         
Shape(id=2)
Shape(id=2):         

test_case: pass!
"""


def test_case_2(self):
    """test Circle.__contains__"""
    # test Circle.__contains__
    ans = "\n" + inspect.stack()[0][3] + ": \n"
    c1 = Circle(0, 0, radius=10)
    c2 = Circle(5, 0, radius=5)
    c3 = Circle(10, 0, radius=5)
    b2 = c2 in c1
    b3 = c3 in c1
    ans += "c2 inside c1 = {:s}.\n".format(str(b2))
    ans += "c3 inside c1 = {:s}.\n".format(str(b3))

    self.check(ans, 4001, True)


TestShapeMethod.test_case_2 = test_case
unittest.main(argv=[''], verbosity=0, exit=False)

TestShapeMethod.test_Circle_contains = None

s = """ 

Expected outputs (except the id numbers and the spaces could be different

test_Circle_contains: 
c2 inside c1 = True.
c3 inside c1 = False.

test_Circle_contains: pass!
"""


def test_case_3(self):
    ans = "\n" + inspect.stack()[0][3] + ": \n"
    c = Circle(0, 0, radius=10)
    c.relocate(2, 2)
    c.moveBy(1, 1)
    ans += str(c) + "\n"
    ans += str(c.details()) + "\n"

    self.check(ans, 4792, True)


TestShapeMethod.test_case_3 = test_case
unittest.main(argv=[''], verbosity=0, exit=False)

s = """
  Expected outputs (except the id numbers and the spaces could be different


test_case: 
Circle(id=366)
Circle(id=366):      area=314, radius: 10.0, center: (3,3)

test_case: pass!        ]
"""


# test Circle.dist
def test_case_4(self):
    ans = "\n" + inspect.stack()[0][3] + ": \n"

    c1 = Circle(0, 0, radius=10)
    c2 = Circle(30, 40, radius=10)
    d = c1.dist(c2)
    ans += "dist = {:.1f}".format(d) + "\n"
    self.check(ans, 1703, True)


TestShapeMethod.test_case_4 = test_case
unittest.main(argv=[''], verbosity=0, exit=False)

s = """ Expected outputs (except the id numbers and the spaces could be different

test_case: 
dist = 30.0

test_case: pass!         ]
"""


# test Point.reloate and Point.dist
def test_case_5(self):
    ans = "\n" + inspect.stack()[0][3] + ": \n"

    p0 = Point(0, 0)
    p1 = Point(0, 0)
    p1.relocate(1, 0)
    d0 = p0.dist(p1)
    p1.relocate(3, 4)
    d1 = p0.dist(p1)
    ans += str(p0) + "\n"
    ans += str(p1) + "\n"
    ans += p0.details() + "\n"
    ans += p1.details() + "\n"
    ans += "d1 = {:.1f}".format(d1)

    self.check(ans, 4158, True)


TestShapeMethod.test_case_5 = test_case
unittest.main(argv=[''], verbosity=0, exit=False)

s = """ Expected outputs (except the id numbers and the spaces could be different

test_case: 
(0,0)
(3,4)
Point(id=30), loc=(0,0)
Point(id=31), loc=(3,4)
d1 = 5.0
test_case: pass!
"""



def test_case_6(self):
    ans = "\n" + inspect.stack()[0][3] + ": \n"

    p = Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])
    ans += str(p) + "\n"
    ans += p.details() + "\n"

    self.check(ans, 6326, True)


TestShapeMethod.test_case_6 = test_case
unittest.main(argv=[''], verbosity=0, exit=False)

s = """ Expected outputs (except the id numbers and the spaces could be different

test_case: 
Polygon(id=49)
Polygon(id=49):       <vertex:(0,0)(10,0)(10,10)(0,10)>, area=100, perimeter=40

test_case: pass!
"""


def test_case_7(self):
    ans = "\n" + inspect.stack()[0][3] + ": \n"

    seg = [(0, 0), (3, 4)]
    s = Segment(seg)
    ans += str(s) + "\n"
    ans += s.details() + "\n"

    self.check(ans, 6715, True)


TestShapeMethod.test_case_7 = test_case

unittest.main(argv=[''], verbosity=0, exit=False)

s = """ Expected outputs (except the id numbers and the spaces could be different

test_case: 
Segment(id=179)
Segment(id=179):      <vertex:(0,0)(3,4)>, length=5 <vertex:(0,0)(3,4)>, length=5

test_case: pass!
"""


def test_case_8(self):
    ans = "\n" + inspect.stack()[0][3] + ": \n"

    s = Triangle([(0, 0), (10, 0), (5, 5)])

    ans += str(s) + "\n"
    ans += s.details() + "\n"

    self.check(ans, 6084, True)


TestShapeMethod.test_case_8 = test_case

unittest.main(argv=[''], verbosity=0, exit=False)

s = """ Expected outputs (except the id numbers and the spaces could be different


test_case: 
Triangle(id=192)
Triangle(id=192):     <vertex:(0,0)(10,0)(5,5)>, area=25, perimeter=24

test_case: pass!
"""


def test_case_9(self):
    ans = "\n" + inspect.stack()[0][3] + ": \n"

    s = Rectangle(width=3, height=4)

    ans += str(s) + "\n"
    ans += s.details() + "\n"

    self.check(ans, 7059, True)


TestShapeMethod.test_case_9 = test_case

unittest.main(argv=[''], verbosity=0, exit=False)

s = """ Expected outputs (except the id numbers and the spaces could be different

test_case: 
Rectangle(id=240)
Rectangle(id=240):    <vertex:(0,0)(3,0)(3,4)(0,4)>, area=12, perimeter=14 <w=3,h=4>

test_case: pass!
"""


def test_case_10(self):
    ans = "\n" + inspect.stack()[0][3] + ": \n"

    s = Rectangle(width=3, height=4)

    ans += str(s) + "\n"
    ans += s.details() + "\n"

    r = Rectangle(0, 0)
    p = Point(1, 1)
    x = r.union(p)
    r.enclose(p)
    r.enclose(Point(2, 2))
    ans += r.details() + "\n"

    self.check(ans, 12087, True)


TestShapeMethod.test_case_10 = test_case

unittest.main(argv=[''], verbosity=0, exit=False)

s = """ Expected outputs (except the id numbers and the spaces could be different
test_case: 
Rectangle(id=202)
Rectangle(id=202):    <vertex:(0,0)(3,0)(3,4)(0,4)>, area=12, perimeter=14 <w=3,h=4>
Rectangle(id=207):    <vertex:(0,0)(2,0)(2,2)(0,2)>, area=4, perimeter=8 <w=2,h=2>

test_case: pass!
"""


def test_case_11(self):
    ans = "\n" + inspect.stack()[0][3] + ": \n"

    x = Square(width=5)
    x.moveBy(5, 5)

    ans += str(x) + "\n"
    ans += x.details() + "\n"

    self.check(ans, 6681, True)


TestShapeMethod.test_case_11 = test_case

unittest.main(argv=[''], verbosity=0, exit=False)

s = """ 
test_case: 
Square(id=327)
Square(id=327):       <vertex:(5,5)(10,5)(10,10)(5,10)>, area=25, perimeter=20 <w=5,h=5>

test_case: pass!
"""


def create(pt, r=None):
    n = len(pt)
    if (r == None):
        if n == 1:
            x, y = pt[0]
            return Point(x, y)
        elif n == 2:
            return Segment(pt)
        elif n == 3:
            return Triangle(pt)
        else:
            return Polygon(pt)
    elif n == 1:
        x, y = pt[0]
        if (r > 0):
            return Circle(x, y, r)
        else:
            return Point(x, y)


Shape.create = staticmethod(create)



def test_case_12(self):
    ans = "\n" + inspect.stack()[0][3] + ": \n"
    pts = [(14, 10), (8, 5), (4, 13), (13, 1), (16, 11), (2, 17), (19, 19), (5, 10), (12, 8), (11, 11)]

    for i in range(5):
        x = Shape.create(pts[:i + 1])
        ans += str(x) + "\n"
        ans += x.details() + "\n"

    self.check(ans, 24635, True)


TestShapeMethod.test_case_12 = test_case

unittest.main(argv=[''], verbosity=0, exit=False)

s = """ 
Expected outputs (except the id numbers and the spaces could be different

test_case: 
(14,10)
Point(id=99), loc=(14,10)
Segment(id=100)
Segment(id=100):      <vertex:(14,10)(8,5)>, length=8 <vertex:(14,10)(8,5)>, length=8
Triangle(id=103)
Triangle(id=103):     <vertex:(14,10)(8,5)(4,13)>, area=34, perimeter=27
Polygon(id=107)
Polygon(id=107):      <vertex:(14,10)(8,5)(4,13)(13,1)>, area=12, perimeter=41
Polygon(id=112)
Polygon(id=112):      <vertex:(14,10)(8,5)(4,13)(13,1)(16,11)>, area=21, perimeter=44

test_case: pass!
"""