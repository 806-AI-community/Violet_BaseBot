import turtle
import numpy as np
import os
import re


class LineMethod(object):
    def __init__(self, width, height):
        # 贝塞尔函数的取样次数
        self.samples = 15
        self.width = width
        self.height = height

    def Bezier(self, p1, p2, t):
        # 一阶贝塞尔函数
        return p1 * (1 - t) + p2 * t

    def Bezier2(self, x1, y1, x2, y2, x3, y3):
        # 二阶贝塞尔函数
        turtle.goto(x1, y1)
        turtle.pendown()
        for t in range(0, self.samples + 1):
            x = self.Bezier(self.Bezier(x1, x2, t / self.samples),
                            self.Bezier(x2, x3, t / self.samples), t / self.samples)
            y = self.Bezier(self.Bezier(y1, y2, t / self.samples),
                            self.Bezier(y2, y3, t / self.samples), t / self.samples)
            turtle.goto(x, y)
        turtle.penup()

    def Bezier3(self, x1, y1, x2, y2, x3, y3, x4, y4):
        # 三阶贝塞尔函数
        x1 = - self.width / 2 + x1
        y1 = self.height / 2 - y1
        x2 = - self.width / 2 + x2
        y2 = self.height / 2 - y2
        x3 = - self.width / 2 + x3
        y3 = self.height / 2 - y3
        x4 = - self.width / 2 + x4
        y4 = self.height / 2 - y4  # 坐标变换
        turtle.goto(x1, y1)
        turtle.pendown()
        for t in range(0, self.samples + 1):
            x = self.Bezier(
                self.Bezier(self.Bezier(x1, x2, t / self.samples), self.Bezier(x2, x3, t / self.samples),
                            t / self.samples),
                self.Bezier(self.Bezier(x2, x3, t / self.samples), self.Bezier(x3, x4, t / self.samples),
                            t / self.samples),
                t / self.samples)
            y = self.Bezier(
                self.Bezier(self.Bezier(y1, y2, t / self.samples), self.Bezier(y2, y3, t / self.samples),
                            t / self.samples),
                self.Bezier(self.Bezier(y2, y3, t / self.samples), self.Bezier(y3, y4, t / self.samples),
                            t / self.samples),
                t / self.samples)
            turtle.goto(x, y)
        turtle.penup()

    def Moveto(self, x, y):
        # 绝对移动
        turtle.penup()
        turtle.goto(- self.width / 2 + x, self.height / 2 + y)
        turtle.pendown()

    def MovetoRelative(self, dx, dy):
        # 相对移动
        turtle.penup()
        turtle.goto(turtle.xcor() + dx, turtle.ycor() - dy)
        turtle.pendown()

    def Line(self, x1, y1, x2, y2):
        # 连接svg坐标下两点
        turtle.penup()
        turtle.goto(- self.width / 2 + x1, self.height / 2 - y1)
        turtle.pendown()
        turtle.goto(- self.width / 2 + x2, self.height / 2 - y2)
        turtle.penup()

    def Lineto(self, x, y):
        # 连接当前点和svg坐标下(x, y)
        turtle.pendown()
        turtle.goto(- self.width / 2 + x, self.height / 2 - y)
        turtle.penup()

    def LinetoRelative(self, dx, dy):
        # 连接当前点和相对坐标(dx, dy)的点
        turtle.pendown()
        turtle.goto(turtle.xcor() + dx, turtle.ycor() - dy)
        turtle.penup()

    def Curveto(self, x1, y1, x2, y2, x, y):
        # 三阶贝塞尔曲线到(x, y)
        turtle.penup()
        X_now = turtle.xcor() + self.width / 2
        Y_now = self.height / 2 - turtle.ycor()
        self.Bezier3(X_now, Y_now, x1, y1, x2, y2, x, y)

    def CurvetoRelative(self, x1, y1, x2, y2, x, y):
        # 三阶贝塞尔曲线到相对坐标(x, y)
        turtle.penup()
        X_now = turtle.xcor() + self.width / 2
        Y_now = self.height / 2 - turtle.ycor()
        self.Bezier3(X_now, Y_now, X_now + x1, Y_now + y1, X_now + x2, Y_now + y2, X_now + x, Y_now + y)

def draw_connection(x,y,n):
    canvas = LineMethod(0,0)
    if(n==4):
        canvas.Moveto(x,y)
        turtle.color("DeepSkyBlue")
        turtle.pensize(3)
        canvas.CurvetoRelative(100,0,100,150,200,150)
        canvas.Moveto(x,y)
        turtle.color("SpringGreen1")
        turtle.pensize(3)
        canvas.CurvetoRelative(100,0,100,50,200,50)
        canvas.Moveto(x,y)
        turtle.color("Chocolate")
        turtle.pensize(3)
        canvas.CurvetoRelative(100,0,100,-50,200,-50)
        canvas.Moveto(x,y)
        turtle.color("Orchid")
        turtle.pensize(3)
        canvas.CurvetoRelative(100,0,100,-150,200,-150)
    elif(n==3):
        turtle.pensize(3)
        turtle.color("Orchid")
        canvas.Moveto(x,y)
        canvas.CurvetoRelative(100,0,100,150,200,150)
        turtle.color("DeepSkyBlue")
        canvas.Moveto(x,y)
        canvas.CurvetoRelative(100,0,150,0,200,0)
        turtle.color("SpringGreen1")
        canvas.Moveto(x,y)
        canvas.CurvetoRelative(100,0,100,-150,200,-150)
    elif(n==2):
        turtle.pensize(3)
        canvas.Moveto(x,y)
        turtle.color("NavajoWhite1")
        canvas.CurvetoRelative(100,0,100,150,200,150)
        canvas.Moveto(x,y)
        turtle.color("SlateBlue1")
        canvas.CurvetoRelative(100,0,100,-150,200,-150)

    elif(n==1):
        turtle.pensize(3)
        canvas.Moveto(x,y)
        canvas.CurvetoRelative(100,0,150,0,200,0)





