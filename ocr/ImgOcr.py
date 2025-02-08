import os
import re

import cv2
import easyocr
import numpy as np
import pandas as pd


# 定义方法传入一个图片路径，返回提取字段信息
def fetch_info(abstract_file_path):
    with open(abstract_file_path, 'rb') as f:
        image_data = f.read()
    # 将二进制数据转换为图像
    image = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)
    # 初始化 EasyOCR 读取器
    reader = easyocr.Reader(['ch_sim', 'en'], gpu=False)
    # 读取文本 detail=0 不输出全部信息，只输出关键信息
    result = reader.readtext(image, detail=0)
    print(result)
    # 正则表达式
    patterns = {
        '姓名': r'姓名:([\u4e00-\u9fa5]+)',
        '身份证号': r'证件号码:(\d{17}[\dX])',
        '账户号': r'账户号:(\d+)',
        '本金总和': r'本金总和:(\d+\.\d+)'
    }
    # 收集提取的信息，导出到excel中
    # 提取信息
    extracted_info = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, '\n'.join(result))
        if match:
            extracted_info[key] = match.group(1)
        else:
            extracted_info[key] = None

    return extracted_info


if __name__ == '__main__':
    all_extracted_info = []
    # 文件夹路径
    dir_path = r'D:\home'
    # 遍历dir_path目录中，包含字符串“客户”且为jpg格式的图片，传入到下面的方法中
    for file_name in os.listdir(dir_path):
        if '客户余额信息' in file_name and (file_name.lower().endswith(".jpg") or file_name.lower().endswith('.png')):
            file_path = os.path.join(dir_path, file_name)
            extracted_info_item = fetch_info(file_path)
            all_extracted_info.append(extracted_info_item)

    # 导出成Excel
    df = pd.DataFrame(all_extracted_info)
    df.to_excel('extract_info.xlsx', index=False)
