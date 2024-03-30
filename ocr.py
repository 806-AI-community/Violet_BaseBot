import sys
import json
import base64
from chat_bot import messages


IS_PY3 = sys.version_info.major == 3
if IS_PY3:
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.error import URLError
    from urllib.parse import urlencode
    from urllib.parse import quote_plus


# 防止https证书校验不正确
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


"""
读取文件
"""
def read_png_file(image_path):
    f = None
    try:
        f = open(image_path, 'rb')
        return f.read()
    except:
        print('read image file fail')
        return None
    finally:
        if f:
            f.close()


"""
调用远程服务
"""
def request(url, data):
    req = Request(url, data.encode('utf-8'))
    has_error = False
    try:
        f = urlopen(req)
        result_str = f.read()
        if (IS_PY3):
            result_str = result_str.decode()
        return result_str
    except  URLError as err:
        print(err)


def upload_png_file(input_file):
    global messages

    # 获取access token
    token = "24.62b65f8f60d40cddaa1bfd39633796e0.2592000.1714189725.282335-58501750"

    OCR_URL = "https://aip.baidubce.com/rest/2.0/ocr/v1/webimage"

    # 拼接通用文字识别高精度url
    image_url = OCR_URL + "?access_token=" + token

    png_text = ""

    # 修改为你自己的图片路径
    png_file_content = read_png_file(input_file)

    # 调用文字识别服务
    result = request(image_url, urlencode({'image': base64.b64encode(png_file_content)}))

    # 解析返回结果
    result_json = json.loads(result)
    # print(result)
    
    for words_result in result_json["words_result"]:
        png_text = png_text + words_result["words"]

    # 打印文字
    # print(png_text)
    # return png_text
    messages.append({"role": "system", "content": "这是刚上传的笔记"+ png_text})

