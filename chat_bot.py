from pathlib import Path
from openai import OpenAI
from style_prompt import style_prompt
import os

file_content=None


client = OpenAI(
    api_key="sk-AOgesgyRQevFmXQU0USfwoQr4HcC8nSGYOcleJrwW8hBxCRc",

    base_url="https://api.moonshot.cn/v1",
)

messages=[
        {
            "role": "system",
            "content": "你是一个806AI助理，具有强大的能力",
        },
]


def change_style(style_choice):
    global messages
    if "传统型" in style_choice:
        messages=style_prompt.messages_traditional
    elif "引导型" in style_choice:
        messages=style_prompt.messages_guiding
    elif "宽松型" in style_choice:
        messages=style_prompt.messages_laissez_faire 


def ask(question):
    # num_of_round = 5
    global messages
    try:
        messages.append({"role": "user", "content": question})
        response = client.chat.completions.create(
            model="moonshot-v1-8k",
            messages=messages,
            temperature=0.3,
        )       
    except Exception as e:
        print(e)
        return e
    message_content = response.choices[0].message.content
    messages.append({"role": "assistant", "content": message_content})
    # if len(messages) > num_of_round * 2 + 1:
    #     del messages[1:3]  # Remove the first round conversation left.
    return message_content


def upload_file(input_file):
    global file_content
    global client
    # 将 NamedString 对象转换为字符串，然后编码为字节流
    file_object = client.files.create(file=Path(input_file), purpose="file-extract")
    # 假设返回的file_object具有id属性
    file_content = client.files.content(file_id=file_object.id).text
    messages.append({"role": "system", "content": file_content})


def respond(ask_message_content,chat_history=[]):
    answer_message_content = ask(ask_message_content)
    chat_history.append((ask_message_content,answer_message_content))
    #chat_hitstory 是一个元组，每一个都是一个自己来回的对话
    return "", chat_history


def sum_file(input_file):
    global file_content

    return file_content