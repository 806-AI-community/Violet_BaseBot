from md_to_mind.turtle_draw import draw_retangle,draw_children
import turtle
from PIL import Image
def read_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    k1=-1
    k2=-1
    k3=0
    markdown_list = []
    current_heading = None

    for line in lines:
        line = line.strip()
        if  line.count('#') == 1:
            k1=k1+1
            k2=-1
            temp_list = []
            content=line[1:]
            temp_list.append(content) 
            markdown_list.append(temp_list)
        elif line.count('#') == 2:
            k2=k2+1
            temp_list = []
            content=line[2:]
            temp_list.append(content) 
            markdown_list[k1].append(temp_list)
            
        elif line.count('#') == 3:
            
            temp_list = []
            content=line[3:]
            temp_list.append(content) 
            markdown_list[k1][k2+1].append(temp_list)

    return markdown_list

def read_content(content):
    markdown_list = []
    k1=-1
    k2=-1
    k3=0
    for line in content:
        line = line.strip()
        if  line.count('#') == 1:
            k1=k1+1
            k2=-1
            temp_list = []
            content=line[1:]
            temp_list.append(content) 
            markdown_list.append(temp_list)
        elif line.count('#') == 2:
            k2=k2+1
            temp_list = []
            content=line[2:]
            temp_list.append(content) 
            markdown_list[k1].append(temp_list)
            
        elif line.count('#') == 3:
            
            temp_list = []
            content=line[3:]
            temp_list.append(content) 
            markdown_list[k1][k2+1].append(temp_list)
    return markdown_list
# 示例用法

""" x_start=-300
y_start=-300  
markdown_list = read_content(file_path)
for i in range(len(markdown_list)):
    print(markdown_list[i][0])
    parent_x=x_start
    parent_y=y_start+i*500
    draw_retangle(parent_x,parent_y,markdown_list[i][0])
    draw_children(parent_x,parent_y,markdown_list[i][1:]) """
# 保存图形为PostScript文件

