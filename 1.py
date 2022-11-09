import requests
import csv
from contextlib import closing#保存csv文件

def save_csv(f_name, data):#1. 创建文件对象

    f = open('./test.csv', 'w', encoding='gbk', newline='') #2. 基于文件对象构建 csv写入对象

    csv_writer = csv.writer(f)#4. 写入csv文件内容

    for row in data:

        csv_writer.writerow(row)#5. 关闭文件

    f.close()#下载csv文件