from openai import OpenAI
client = OpenAI(
    api_key="sk-AOgesgyRQevFmXQU0USfwoQr4HcC8nSGYOcleJrwW8hBxCRc",
    base_url="https://api.moonshot.cn/v1",
)
messages=[
    {
        "role": "system",
        "content": "总结用户输入的文本内容，并严格以特定形式输出，不需要输出除总结外的其他内容，每行文本前必须有相对的井号，井号后面不需要空格，井号和内容之间也不需要空格，内容与内容之间不能有空行，段落之间不能有空行，不能有空行。根据逻辑关系确定确定每行前的井号个数。例如：#一级标题##二级标题#一级标题#一级标题##二级标题###三级标题",
    },
]



# 使用示例
def save_string_to_md(content, filename="output.md"):
    # content = kimi_respend
    # 确保文件名以.md结尾
    if not filename.endswith(".md"):
        filename += ".md"
    
    # 写入文件
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    
    # 返回文件路径
    return filename


message = input("You: ")  
messages.append({"role":"user","content":message})  

response = client.chat.completions.create(
    model="moonshot-v1-8k",
    messages=messages
)
print("Kimi: ", response.choices[0].message.content)  

