user@3G-10:~/src/oo-drawing$ python3
Python 3.5.2 (default, Nov 12 2018, 13:43:14)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> python3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'python3' is not defined
>>> import cs1graphics as cg
>>> paper = cg.Canvas()
>>> paper.setBackgroundColor('SkyBlue)
  File "<stdin>", line 1
    paper.setBackgroundColor('SkyBlue)
                                     ^
SyntaxError: EOL while scanning string literal
>>> paper.setBackgroundColor('SkyBlue')
>>> paper.setWidth(800)
>>> paper.setHeight(600)
>>> paper.setTitle("My World")
>>> paper.
paper.__class__(            paper._height
paper.__contains__(         paper._mouseCoordinates
paper.__delattr__(          paper._reference
paper.__dict__              paper._title
paper.__dir__(              paper._transform
paper.__doc__               paper._update(
paper.__eq__(               paper._width
paper.__format__(           paper.add(
paper.__ge__(               paper.addHandler(
paper.__getattribute__(     paper.clear(
paper.__gt__(               paper.close(
paper.__hash__(             paper.getAutoRefresh(
paper.__init__(             paper.getBackgroundColor(
paper.__le__(               paper.getContents(
paper.__lt__(               paper.getHeight(
paper.__module__            paper.getMouseCoordinates(
paper.__ne__(               paper.getTitle(
paper.__new__(              paper.getWidth(
paper.__reduce__(           paper.open(
paper.__reduce_ex__(        paper.refresh(
paper.__repr__(             paper.remove(
paper.__setattr__(          paper.removeHandler(
paper.__sizeof__(           paper.rotateView(
paper.__str__(              paper.saveToFile(
paper.__subclasshook__(     paper.setAutoRefresh(
paper.__weakref__           paper.setBackgroundColor(
paper._animation            paper.setHeight(
paper._backgroundColor      paper.setTitle(
paper._canvasOpen           paper.setView(
paper._contents             paper.setWidth(
paper._forceClose(          paper.translateView(
paper._frozen               paper.wait(
paper._getProperties(       paper.zoomView(
>>> paper.dir(paper)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Canvas' object has no attribute 'dir'
>>> dir(paper)
['__class__', '__contains__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_animation', '_backgroundColor', '_canvasOpen', '_contents', '_forceClose', '_frozen', '_getProperties', '_height', '_mouseCoordinates', '_reference', '_title', '_transform', '_update', '_width', 'add', 'addHandler', 'clear', 'close', 'getAutoRefresh', 'getBackgroundColor', 'getContents', 'getHeight', 'getMouseCoordinates', 'getTitle', 'getWidth', 'open', 'refresh', 'remove', 'removeHandler', 'rotateView', 'saveToFile', 'setAutoRefresh', 'setBackgroundColor', 'setHeight', 'setTitle', 'setView', 'setWidth', 'translateView', 'wait', 'zoomView']
>>> paper.getBackgroundColor()
SkyBlue
>>> paper.getWidth()
800
>>> sun = cg.Circle()
>>> paper.add(sun)
>>> sun.setFillColor('yellow')
>>> sun.setRadius(50)
>>> sun.moveTo(700,100)
>>> sunCenter = cg.Point(700,100)
>>> sun2 = cg.Circle(50, sunCenter
... sun2 = cg.Circle(50, sunCenter)
  File "<stdin>", line 2
    sun2 = cg.Circle(50, sunCenter)
       ^
SyntaxError: invalid syntax
>>> sun2 = cg.Circle(50, sunCenter)
>>> sun2 = cg.Circle(50, cg.Point(700,100))
>>> sun2.setFillColor('lightYellow')
>>> paper.add(sun2)
>>> facade = cg.Square(200, cg.Point(400, 350))
>>> facade.setFillColor("white")
>>> paper.add(facade)
>>> chimney = cg.Regtangle(50,70, cg.Point(450,215))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'cs1graphics' has no attribute 'Regtangle'
>>> chimney = cg.Rectangle(50,70, cg.Point(450,215))
>>> chimney.setFillColor('red')
>>> paper.add(chimney)
>>> tree = cg.Polygon(cg.Point(150,220), cg.Point(120,380),cg.Point(180,380))
>>> tree.setFillColor('darkGreen')
>>> paper.add(tree)
>>> sunraySW = cg.Path(cg.Point(660, 140), cg.Point(635,165))
>>> sunraySW.setBordercOLOR("yellow")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Path' object has no attribute 'setBordercOLOR'
>>> sunraySW.setBorderColor("yellow")
>>> sunraySW.setBorderWidth(6)
>>> paper.add(sunraySW)
>>> sunraySW = cg.Path(cg.Point(740, 140), cg.Point(765,165))
>>> sunraySW.setBorderColor("yellow")
>>> sunraySW.setBorderWidth(6)
>>> paper.add(sunraySE)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sunraySE' is not defined
>>> paper.add(sunraySE)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sunraySE' is not defined
>>> sunraySE = cg.Path(cg.Point(740, 140), cg.Point(765,165))
>>> sunraySE.setBorderColor("yellow")
>>> sunraySE.setBorderWidth(6)
>>> paper.add(sunraySE)
>>> sunrarayNE = cg.Path(cg.Point(740,60), cg.Point(765,35)
... sunrayNE = cg.Path(cg.Point(740,60), cg.Point(765,35)
  File "<stdin>", line 2
    sunrayNE = cg.Path(cg.Point(740,60), cg.Point(765,35)
           ^
SyntaxError: invalid syntax
>>> sunrayNE = cg.Path(cg.Point(740,60), cg.Point(765,35))
>>> sunrayNE = set.BorderColor("yellow")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: type object 'set' has no attribute 'BorderColor'
>>> sunrayNE.setBorderColor("yellow")
>>> sunrayNE.setBorderWidth(6)
>>> paper.add(sunrayNE)
>>> sunrayNW = cg.Path(cg.Point(660,60), cg.Point(635,35))
>>> sunrayNW.setBorderColor("yellow")
>>> sunrayNW.setBorderWidth(6)
>>> paper.add(sunrayNW)
>>> chimney.getDepth()
50
>>> grass = cg.Rectangle(800,300,cg.Point(400,450))
>>> grass.setFillColor('green')
>>> grass.setBorderColor('green')
>>> grass.setDepth(75)
>>> paper.add(grass)
>>> grass.setDepth(20)
>>> grass.setDepth(75)
>>> window = cg.Rectangle(50)
>>> window = cg.Rectangle(50, cg.Point(400,350))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/user/src/oo-drawing/cs1graphics.py", line 3842, in __init__
    raise TypeError('height must be numeric')
TypeError: height must be numeric
>>> window = cg.Rectangle(50,70, cg.Point(400,350))
>>> window.setFillColor('Black')
>>> paper.add(window)
>>> roof = cg.Rectangle(250, cg.Point(350,250))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/user/src/oo-drawing/cs1graphics.py", line 3842, in __init__
    raise TypeError('height must be numeric')
TypeError: height must be numeric
>>> roof = cg.Rectangle(250,50 cg.Point(350,250))
  File "<stdin>", line 1
    roof = cg.Rectangle(250,50 cg.Point(350,250))
                                ^
SyntaxError: invalid syntax
>>> roof = cg.Rectangle(250,50, cg.Point(350,250))
>>> roof.setFillColor("pink")
>>> paper.add(roof)
>>> roof = cg.Rectangle(250,50, cg.Point(350,350))
>>> paper.add(roof)
