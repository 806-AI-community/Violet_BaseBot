from openai import OpenAI
from md_to_mind.to_mind import read_content
from md_to_mind.turtle_draw import draw_retangle,draw_children
client = OpenAI(
    api_key="sk-AOgesgyRQevFmXQU0USfwoQr4HcC8nSGYOcleJrwW8hBxCRc",
    base_url="https://api.moonshot.cn/v1",
)
messages=[
    {
        "role": "system",
        "content": "总结用户输入的文本内容，并严格以特定形式输出，不需要输出除总结外的其他内容，每行文本前必须有相对的井号，井号后面不需要空格，\
            井号和内容之间也不需要空格，内容与内容之间不能有空行，段落之间不能有空行，不能有空行。根据逻辑关系确定确定每行前的井号个数。\
                例如：#一级标题##二级标题#一级标题#一级标题##二级标题###三级标题",
    },
]


message = input("You: ")  
messages.append({"role":"user","content":message})  

response = client.chat.completions.create(
    model="moonshot-v1-8k",
    messages=messages
)
kimi_respend=response.choices[0].message.content
print("Kimi: ", kimi_respend)  

x_start=-300
y_start=-300  
markdown_list = read_content(kimi_respend)
for i in range(len(markdown_list)):
    print(markdown_list[i][0])
    parent_x=x_start
    parent_y=y_start+i*500
    draw_retangle(parent_x,parent_y,markdown_list[i][0])
    draw_children(parent_x,parent_y,markdown_list[i][1:])