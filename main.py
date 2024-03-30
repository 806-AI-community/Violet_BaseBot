import gradio as gr
from chat_bot import ask
from chat_bot import upload_file
from chat_bot import respond
from chat_bot import change_style
from ocr import upload_png_file
from speak_chat_bot import speak_ask
from speak_chat_bot import speak_respond
# from chat_bot import sum_file

#test

with gr.Blocks(title="AI知识库学习平台") as demo:

    gr.Markdown("欢迎来到AI知识库学习平台，高效为您解答疑惑")

    with gr.Tab("上传文档，和你共同学习"):
        gr.Markdown("""
                    我们提供新一代的个人知识库管理平台，帮助你更好的学习，更好的总结，更好的提问，更好的回答，更好的进步
                    我们可以实现以下功能：
                    提供更高效的知识管理方式，上传手写笔记，上传文档，上传图片，我们可以给你构建思维导图，给你推荐资料
                    
                    基于这些进行提问，回答，总结，推荐资料等等
                    你可以在这里上传各类你有疑惑的文档，甚至手写笔记的图片，我们会为你解答疑惑，巩固知识""")
        with gr.Row():
            with gr.Column(scale=4):
                chatbot = gr.Chatbot(label="")
                msg = gr.Textbox(placeholder="请输入问题",label="")
                clear = gr.ClearButton([msg, chatbot])
            with gr.Column(scale=1):
                button = gr.UploadButton("上传文档",scale=1)
                button.upload(fn=upload_file, inputs=[button])
                # sum_button = gr.Button("总结文档",scale=1)
                # sum_button.click(sum_file, inputs=[button], outputs="text")
                button_png = gr.UploadButton("上传图片",scale=1)
                button_png.upload(fn=upload_png_file, inputs=[button_png])
                style_choice=gr.Radio(["传统型", "引导型", "宽松型"], label="请选择老师风格", info="不选择默认为宽松型",scale=2)

            msg.submit(respond, [msg, chatbot], [msg, chatbot]) 
            style_choice.change(fn=change_style, inputs=style_choice,outputs=None)


    with gr.Tab("语音对话，和你畅所欲言"):
        gr.Markdown("你可以在这里用语音与AI闲聊、提问，畅所欲言，AI会一直听着你的话，陪着你o(*￣▽￣*)ブ")
        with gr.Column():
            speak_chatbot = gr.Chatbot()
            speak_msg = gr.Textbox()
            speak_clear = gr.ClearButton([speak_msg, speak_chatbot])
            speak_msg.submit(speak_respond, [speak_msg, speak_chatbot], [speak_msg, speak_chatbot]) 
## 添加情绪分析 学习记忆

    with gr.Tab("资料推荐，和你共同进步"):
        gr.Markdown("题不够做？资料不够看？不知道从哪里开始学习？这里有为你推荐的资料，帮助你更好的学习")
        with gr.Column():
            gr.Markdown("推荐资料")

    with gr.Tab("分析结构，促进深度记忆"):
        gr.Markdown("AI知识库")

    with gr.Tab("社区互动，分享你的知识"):
        gr.Markdown("AI知识库")

    with gr.Tab("我的知识库"):
        gr.Markdown("AI知识库")

    with gr.Tab("我的状态"):
        gr.Markdown("AI知识库")
    
    

demo.launch()
# demo.launch(server_name="115.25.46.34", server_port=8080)     