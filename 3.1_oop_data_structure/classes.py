import math, copy, re


class Shape:
    """Base class for various geometric shapes"""
    __count = 0  # Global private variable to keep tracking the shape ID

    def __init__(self):  # constructor
        """__id == __count """
        self.__id = Shape.__count
        Shape.__count += 1

    @property
    def id(self):  # xxx implement the getter of the private variable __id
        """Object id = the number of the Shape object created so far"""
        return self.__id

    def details(self):
        """Detailed description of the boject on top of __str__"""
        name = self.__class__.__name__
        x = "{:s}(id={:d}): ".format(name, self.id)  # string : integered data
        s = "{:20s} ".format(x)  # 20 digited string -right aligned-: integered format
        return s

    def __str__(self):  # xxx implement the following
        """A  string representation of the object in the form of 'Shape(id=n)', where n is a number"""
        return "{:s}(id={:d})".format(self.__class__.__name__, self.__id)  # class name and id



class Circle(Shape):
    """Child class of Shape"""

    def __init__(self, x=0, y=0, radius=0):
        """Shape with center and radius."""
        super().__init__()  # Inherit shape class
        self.__x = x
        self.__y = y
        self.__radius = radius
        """This constructor assigns x,y of center and radius"""

    # xxx: implement the following three methods
    @property
    def x(self):  # xxx:  the getter method of __x
        return self.__x

    @property
    def y(self):  # xxx:  the getter method of __y
        return self.__y

    @property
    def radius(self):  # xxx:  the getter method of __radius
        return self.__radius

    # xxx: implement the following
    def __contains__(self, other):  # overload the boolean operator in
        """Overload boolean operator in
           check if Circle 'self' contains another 'Point' or  'Circle'
        """
        # Don't add the @property in order to use proper codes
        distance = math.sqrt(pow((self.x - other.x), 2) + pow((self.y - other.y), 2))
        # distance btween two circles

        return (
                           distance + other.__radius) <= self.__radius  # Returns True if self contains other's center or points, else False

    # xxx: implement the following
    def area(self):
        """The area of Circle"""
        return math.pi * self.__radius ** 2  # Area = pi * radius^2

    # xxx: implement the following
    def perimeter(self):
        """The perimeter of Circle"""
        return 2 * math.pi * self.__radius  # Perimeter = Circumference = 2 * pi * radius

    def dist(self, other):
        """the distance between Circle self and Circle (or Point) other  """
        if other.__class__ == Circle or other.__class__.__bases__[0] == Circle:
            x = self.x - other.x
            y = self.y - other.y
            d = math.sqrt(x * x + y * y) - self.__radius - other.__radius
            # If the 'd' is positive, two object is not contacted at all
            d = max(d, 0)
            # distance between two circles
            return d
        else:
            return None

    def overlap(self, other):
        """Two circles (or Points) overlap if their distance is 0."""
        d = self.dist(other)
        return d != None and d <= 0

        # xxx: implement the function below

    def enclose(self, pt):
        self.__radius = max(self.__radius, self.dist(pt))
        """ Check if distance to pt is <= radius (if pt is contained in circle)
        If not, extend the circle to the distance between center and the pt (min distance)
        """

    # xxx: implement the setter methods for both x and y together
    # qqq: is this method better than two separate setter methods?
    def relocate(self, x, y):
        """Relocate self.__center to (x,y)"""
        ##the x and y is not method. They are perimeter variable
        self.__x = x
        self.__y = y

    # xxx: implement the function below
    def moveBy(self, dx, dy):
        """add the displacement (dx, dy) to the current center location"""
        self.__x += dx
        self.__y += dy

    def details(self):
        """ override Shape.details"""
        s = super().details()
        s += "area={:.0f}".format(self.area())
        s += ", radius: {:.1f}".format(self.radius)  ##show 1 decimal digit
        s += ", center: ({:d},{:d})".format(self.x, self.y)
        return s


class Point(Circle):
    """A special Circle with radius = 0, thus it is a child class of Circle."""

    # xxx: must make use of the parent class constructor
    def __init__(self, x, y):
        """Initialized private instance variables __x and __y """
        super().__init__(x, y, 0)  # radius = 0 inherit circle

    def cross_product(self, o):
        """helper function to compute the polygon area."""
        x = self.x * o.y
        y = self.y * o.x
        return x - y

    def __str__(self):  # override the inherited function from the parent class
        """a string representation of the object"""
        s = "({:d},{:d})".format(self.x, self.y)
        return s

    def details(self):  # override the inherited function from the parent class
        """a string representation of the object"""
        s = super().__str__()
        s += ", loc=({:d},{:d})".format(self.x, self.y)
        return s


class Polygon(Shape):
    """A Child class of Shape.
       A convex polygon represented as a list of vertices of class Point.
       To compute the area correctly, the polygon has to be convex
    """

    def __init__(self, inputs):
        """inputs is a list of tuples like  [ (x1,y1), (x2,y2), ... ]
           Convert inputs to be a list of Points as the Polygon vertices
        """
        super().__init__()
        n = len(inputs)
        self.__vertex = []
        for i, j in inputs:
            self.__vertex.append(Point(i, j))

    # qqq: What happen if we simply return self.__vertex without make a deepcopy
    # You will return a reference to the same object stored in this class
    # The object stored in the class can be changed outside of the class
    def vertex(self, i):
        return copy.deepcopy(self.__vertex[i])

    # xxx: implement the following
    def relocate_a_vertex(self, i, x, y):
        """relocate vertex i to the new location (x,Y)"""
        if (i > 0 and i < len(self.__vertex)):  # Point = self.__vertex[i]
            self.__vertex[i].relocate(x, y)  # Relocate the Point- private list.setter method()
            # self.__vertex[i].x = x # Change all x points of vertices
            # self.__vertex[i].x = y # Change all y points of vertices

    # xxx: implement the following
    def relocate(self, x, y):
        """relocate the polygon to (x,y) by moving all the vertices together such that
           vertex[0] is located at (x,y) and all other vertices will be relocated with the same displacement dx, and dy
           hints: moveBy
        """
        dx = x - self.__vertex[0].x  # Distance of x relocation
        dy = y - self.__vertex[0].y  # Distance of y relocation
        self.moveBy(dx, dy)  # Move all vertices

    # xxx: implement the following
    def moveBy(self, dx, dy):
        """add an offset (dx,dy) to each vertex of  Polygon"""

        # xxx: make use of the Point.moveBy method

        for v in self.__vertex:  # Get each vertex from list (will call point.moveBy method for each vertex)
            v.moveBy(dx, dy)  # We inherit moveBy from Point which inherits from Circle: Point.moveBy

    # xxx: implement the following
    def area(self):

        # xxx: have to make use of the Point.cross_product(q) method
        area = 0
        for i in range(0, self.__len__()):
            # Point = self.__vertex[i]
            if (i == self.__len__() - 1):  # If last index
                area += self.__vertex[i].cross_product(self.__vertex[0])  # Point = self.__vertex[i]
            else:
                area += self.__vertex[i].cross_product(self.__vertex[i + 1])  # Point = self.__vertex[i]

        return abs(area / 2)  # Area cannot be negative

    def __len__(self):
        """The number of vertices of the polygon"""
        return len(self.__vertex)

    # xxx: implement the following
    def perimeter(self):
        """The sum of all side length of Polygon"""
        perimeter = 0

        for i in range(0, self.__len__()):
            perimeter += self.side_length(i)  # Sum up length of all sides
        return perimeter

    # xxx: implement the following
    def side_length(self, i=0):
        """The length of the side from vertex i to the next"""  # have to make use of the Point.dist method

        if (i == self.__len__() - 1):  # If indexing last vertex
            return self.__vertex[i].dist(self.__vertex[0])  # Point = self.__vertex[i] - uses self as a param
        else:
            return self.__vertex[i].dist(self.__vertex[i + 1])  # Point = self.__vertex[i] - uses self as a param

    def details(self):
        """Detailed description about Polygon"""
        s = super().details()
        s += " <vertex:"
        for p in self.__vertex:
            s += str(p)
        s += ">"
        n = len(self.__vertex)
        if (n > 2):
            s += ", area={:.0f}".format(self.area())
            s += ", perimeter={:.0f}".format(self.perimeter())
        elif n == 2:
            s += ", length={:.0f}".format(self.perimeter() / 2.0)
        return s


class Segment(Polygon):
    # xxx implement the following
    def __init__(self, pts):
        super().__init__(pts)  # make use of the parent __init__ method

    def details(self):
        """To override the Polygon.details()"""
        s = super().details()
        s += " <vertex:"
        for i in range(2):
            p = self.vertex(i)
            s += str(p)
        s += ">"
        s += ", length={:.0f}".format(self.perimeter() / 2.0)
        return s

class Triangle (Polygon):
    #xxx implement the following
    def __init__ (self, pts):
        super().__init__(pts) # make use of the parent __init__ method


class Rectangle(Polygon):
    # xxx: have to invoke __init__ of the parent class Polygon
    # xxx: cannot have any local variable

    def __init__(self, x=0, y=0, width=0, height=0):
        p0 = (0, 0)
        p1 = (width, 0)
        p2 = (width, height)
        p3 = (0, height)
        ## assign each vertex of rectangle
        super().__init__([p0, p1, p2, p3])

    # qqq: Should we implement it in the child class Rectangle

    def __contains__(self, other):
        """Check if Rectangle self contains Rectangle or Point other """
        p, q = self.vertex(0), self.vertex(2)

        if other.__class__ == Point:
            a = other.x
            b = other.y
        else:
            p, q = other.vertex(0), other.vertex(2)

        return a.x >= p.x and b.x <= q.x and a.y >= p.y and b.y <= q.y

    # xxx: extend Rectangle minimally to contain a given polygon
    def enclose(self, other):
        """Enlarge Rectangle to contain a given polygon 'other'
            with the minimum increase of the rectangular area
        """
        enclosedRectangle = self.union(other)
        # union integrates object other and self

        for i in range(self.__len__()):  # Relocate vertices
            self.relocate_a_vertex(i, enclosedRectangle.vertex(i).x, enclosedRectangle.vertex(i).y)

    # xxx: implement the following
    def __add__(self, other):
        """Overload the operator + as the union of two Rectangles """
        # return self.union(other)
        self = self.union(other)  # Modify self

    # xxx: implement the following
    def __and__(self, other):
        """Overload the operator & as the intersection of two Rectangles """
        # return self.intersection(other)
        self = self.intersection(other)  # Modify self

    def union(self, other):
        """Get the smallest rectangle that contains both rectangles self and other
        """
        p0, p1 = self.vertex(0), self.vertex(2)

        if other.__class__ == Point:
            q0 = q1 = other

        else:
            q0, q1 = other.vertex(0), other.vertex(2)

        min_x = min(p0.x, q0.x)
        max_x = max(p1.x, q1.x)
        min_y = min(p0.y, q0.y)
        max_y = max(p1.y, q1.y)
        w = max_x - min_x
        h = max_y - min_y
        r = None

        if (w >= 0 and h >= 0):

            if w == h:
                r = Square(width=w)

            else:
                r = Rectangle(width=w, height=h)

            r.relocate(min_x, min_y)
        return r

    # xxx: implement the following
    def intersection(self, other):
        """Get the intersected area of Rectangles self and other
           Return None if no intersection
        """
        p0, p1 = self.vertex(0), self.vertex(2)
        ##copy vertex(index)

        if other.__class__ == Point:
            q0 = q1 = other

        else:
            q0, q1 = other.vertex(0), other.vertex(2)
        max_x = max(p0.x, q0.x)
        min_x = min(p1.x, q1.x)
        max_y = max(p0.y, q0.y)
        min_y = min(p1.y, q1.y)

        w = abs(min_x - max_x)
        h = abs(min_y - max_y)

        r = None
        if (w <= 0 and h <= 0):  # Switch signs
            if w == h:
                r = Square(width=w)
            else:
                r = Rectangle(width=w, height=h)
            r.relocate(max_x, max_y)
        return r

    # xxx: implement the following
    def overlap(self, other):
        """return True if Rectangle self and other intersect"""
        return self.intersection(other) == None  # Returns None if no intersection

    def width(self):
        """The width of a rectangle = the length of side 0 (from vertex 0 to vertex 1)."""
        return self.side_length(0)

    # xxx: implement the following
    def height(self):
        """The height of a rectangle = the length of side 1(from vertex 1 to vertex 2). """
        return self.side_length(1)  # Length between vertex[1] and vertex[2]

    def details(self):
        """Override the same function in the parent class"""
        s = super().details()
        w = self.width()
        h = self.height()
        s += " <w={:.0f},h={:.0f}>".format(w, h)
        return s


class Square (Rectangle):
    # xxx implement the following
    def __init__ (self,  x=0,y=0,width=0):
        """Override the same function in the parent class"""
        super().__init__( x,y, width, width) #xxx must make use of the __init__ method of super class
    #xxx do not add and other instance methods or variables except __init__