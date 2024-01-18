import requests
import re
from datetime import datetime

url = "http://www.weather.com.cn/weather1dn/101100713.shtml"

# 获取当前时间
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 发送 HTTP 请求获取网页源码
response = requests.get(url)

if response.status_code == 200:
    # 使用正则表达式提取od26后面的数字
    pattern = re.compile(r'"od26":"([-+]?\d*\.\d+|\d+)"')
    matches = pattern.findall(response.text)

    # 将提取到的数字追加到文本文件末尾
    with open("output.txt", "a") as file:
        # 在文件开头加入当前时间
        file.write(f"{current_time}\n")

        for match in matches:
            od26_number = float(match)
            # 写入数据
            file.write(f"{od26_number}\n")
if response.status_code == 200:
    # 使用正则表达式提取od21和od22后面的数字
    pattern = re.compile(r'"od21":"([-+]?\d*\.\d+|\d+)","od22":"([-+]?\d*\.\d+|\d+)"')
    matches = pattern.findall(response.text)

    # 获取当前时间
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 将提取到的数字追加到文本文件末尾，分为两列，一一对应
    with open("output.txt", "a") as file:
        for match in matches:
            od21_number = float(match[0])
            od22_number = float(match[1])
            file.write(f"{od21_number}  {od22_number}\n")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
