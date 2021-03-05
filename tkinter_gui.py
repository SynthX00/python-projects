from tkinter import *
import random

class Point:
    points = [] #existing points
    draggable = None
    isDragging = False

    def __init__(self,cv, x, y, radius, color: str) -> None:

        self.dir = 1 #right
        self.radius = radius
        self.canvas = cv
        self.x, self.y = x,y
        self.object = self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, outline='')
        self.line = None
        Point.points.append(self)

        #create line
        self.createLines()

    def __repr__(self) -> str:
        return "({},{})".format(self.x, self.y)

    @classmethod
    def printPoints(cls):
        for p in cls.points:
            print(p)

    def move(self):
        
        if(Point.draggable == self):
            return

        if(self.x + self.radius*2 >= self.canvas.winfo_width()):
            self.dir = -1
        elif(self.x <= 0):
            self.dir = 1

        self.canvas.move(self.object, 1*self.dir, 0)
        self.x, self.y = self.canvas.coords(self.object)[:2]
        self.x += self.radius
        self.y += self.radius
    
    def checkHit(self, x, y, rad = None) -> tuple:
        
        if(rad == None):
            rad = self.radius
        
        #check if x,y is inside point
        if( (x >= self.x - rad) and (y >= self.y - rad) and
            (x <= self.x + rad) and (y <= self.y + rad)):
            return (True, self)

        return (False, None)

    def moveTo(self, x, y):

        self.canvas.coords(self.object, x - self.radius, y - self.radius, x + self.radius, y + self.radius)

        #move line
        if (not self.line == None):
            if (self.line.points[0] == self): #check if start or end point in the line
                self.line.canvas.coords(self.line.object, x, y, self.line.points[1].x, self.line.points[1].y)
            else:
                self.line.canvas.coords(self.line.object, self.line.points[0].x, self.line.points[0].y, x, y)

        #save current position
        self.x, self.y = self.canvas.coords(self.object)[:2]
        self.x += self.radius
        self.y += self.radius

    @classmethod
    def createLines(cls):

        if(len(cls.points)%2 == 0): #even number of points
            for i in range(len(cls.points)-1, -1, -2):
                if((cls.points[i].line == None) and cls.points[i-1].line == None):
                    _line = Line(cls.points[i].canvas, cls.points[i-1], cls.points[i], 2)
                    cls.points[i].line = _line
                    cls.points[i-1].line = _line


class Line:
    lines = [] #existing lines

    def __init__(self, cv, start, end, width) -> None:
        
        self.points = (start, end)
        self.canvas = cv
        self.object = self.canvas.create_line(start.x, start.y, end.x, end.y, width=str(width), fill='white')
        Line.lines.append(self)
    
    def __repr__(self) -> str:
        return '{}'.format(self.canvas.coords(self.object))

    @classmethod
    def printLines(cls):

        for l in cls.lines:
            print(l)
        
    

window = Tk()

width, height = 500, 500
window.geometry('{}x{}'.format(width,height))
window.resizable(False, False)
window.configure(bg='black')

canvas = Canvas(window, width=width, height=height)
canvas.configure(bg='black')
canvas.pack()

colors = ['white', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']

def placePoint(event):

    _hit = (False, None)
    for p in Point.points:
        _hit = p.checkHit(event.x, event.y, 10)
        if(_hit[0]):
            break

    if(not _hit[0]):
        Point(canvas, event.x, event.y,5, colors[random.randint(0, len(colors)-1)])

    Line.printLines()

def startDrag(event):

    if (not Point.isDragging and Point.draggable == None):
        print('mouse @ ({},{})'.format(event.x, event.y))
        #Point.printPoints()
        for p in Point.points:
            _hit = p.checkHit(event.x, event.y)
            if(_hit[0]):
                Point.draggable = _hit[1]
                Point.isDragging = True
                print('dragging point @ ({},{})'.format(_hit[1].x,_hit[1].y))
                break

def endDrag(event):

    Point.draggable = None
    Point.isDragging = False
    print('drag end\n_______________')
    

def dragPoint(event):

    #print('{} : {}'.format(Point.isDragging, Point.draggable))
    if (Point.isDragging):
        Point.draggable.moveTo(event.x, event.y)

def update() -> None:

    #for p in Point.points:
    #    p.move()
    window.after(15, update)

#a = Point(canvas, 100,100, 5, 'red')
#b = Point(canvas, 400,400, 5, 'red')
#Line(canvas, a, b, 3)

canvas.bind('<Button-3>', placePoint)
canvas.bind('<Button-1>', startDrag)
canvas.bind('<Motion>', dragPoint)
canvas.bind('<ButtonRelease-1>', endDrag)

window.after(15, update)
window.mainloop()