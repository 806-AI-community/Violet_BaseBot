from turtle import *
import turtle
from bezier import draw_connection
import math
""" 
假设一级有两个
二级三个
三级2个

 """
n1=2
n2=3
n3=2
width=80
length=180
def draw_retangle(x,y,info):
    turtle.speed(9)
    turtle.pensize(1)
    turtle.color("black")
    content_len=len(info)
    lines_len=math.ceil(content_len/8)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor("PapayaWhip")   #填充颜色
    turtle.begin_fill()    #开始填充
    for i in range(1,5):
        if i % 2 == 1:     #取余数为1则长为200,否则长为120
            d = length
        else:
            d = width+lines_len*5
        turtle.forward(d)
        turtle.left(90)    #逆时针90度 

    turtle.end_fill()      #结束填充
    turtle.penup()
    turtle.pencolor('black')
    for i,ch in enumerate(info):
        if(i%8==0):
            lines_id=math.ceil(i/8)
            turtle.goto(x+10,y+30+lines_len*10-lines_id*19)
        turtle.write(ch, font=('KaiTi',15,'normal'))
        
        turtle.fd(20)

def calculate_children_xy(parent_x,parent_y,children_num):
    children_xy=[]
    if(children_num==4):
        for i in range(4):
            children_xy.append((parent_x+375,parent_y-150+100*i))
    elif(children_num==3):
        for i in range(3):
            children_xy.append((parent_x+375,parent_y-150+150*i))
    elif(children_num==2):
        for i in range(2):
            children_xy.append((parent_x+375,parent_y-150+280*i))
    elif(children_num==1):
        for i in range(1):
            draw_retangle(parent_x+375,parent_y)
    else:
        children_xy=None
    return children_xy


def draw_line(parent_x,parent_y,children_num,info):
    parent_right_x=parent_x+length
    parent_right_y=parent_y+width/2
    children_xy=calculate_children_xy(parent_x,parent_y,children_num)

    turtle.penup()
    turtle.goto(parent_right_x,parent_right_y)
    turtle.pendown()
    draw_connection(parent_right_x,parent_right_y,children_num)
    for i in range(children_num):
        child_xy=children_xy[i]
        start_x=child_xy[0]+length
        start_y=child_xy[1]+width/2
        turtle.penup()
        turtle.goto(start_x,start_y)
        turtle.pendown()
        draw_retangle(child_xy[0],child_xy[1],info[i])


def draw_children(parent_x,parent_y,children):
    #turtle.showturtle()   #显示画笔
    children_info=[]
    children_num=len(children)
    
    if(type(children[0])==str):
        children=children[1:]
        children_num=len(children)
    children_xy=calculate_children_xy(parent_x,parent_y,children_num)
    for i in range(children_num):
        if(len(children[i])!=1):
            children_info.append(children[i][0])
            draw_children(children_xy[i][0],children_xy[i][1],children[i])
        else:
            children_info.append(children[i])
    draw_line(parent_x,parent_y,children_num,children_info)




