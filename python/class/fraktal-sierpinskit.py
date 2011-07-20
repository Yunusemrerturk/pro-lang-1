#!/usr/bin/pyhton

from graphics import *
import time 

def sierpinskiT(points, level, win):
        colormap = ['blue','red','green','white','yellow','violet','orange']
        p=Polygon(points)
        p.setFill(colormap[level])
        p.draw(win)
        time.sleep(0.3)
        if level>0:
                sierpinskiT([points[0], getMid(points[0], points[1]), getMid(points[0], points[2])], level-1, win)
                sierpinskiT([points[1], getMid(points[0], points[1]), getMid(points[1], points[2])], level-1, win)
                sierpinskiT([points[2], getMid(points[2], points[1]), getMid(points[0], points[2])], level-1, win)

def getMid(p1, p2):
        return Point( ((p1.getX()+p2.getX()) / 2.0), ((p1.getY()+p2.getY()) / 2.0) )

if __name__=='__main__':
        win = GraphWin('st', 500, 500)
        win.setCoords(20, -10, 80, 50)
        myPoints=[Point(25, 0), Point(50, 43.3), Point(75, 0)]
        sierpinskiT(myPoints, 3, win)
        win.getMouse()

