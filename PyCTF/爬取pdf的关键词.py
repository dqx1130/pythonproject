import requests
from bs4 import BeautifulSoup
import os
import re
import hashlib
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.layout import *
from pdfminer.converter import PDFPageAggregator


# 将pdf转换为txt的函数
def pdf2txt(path):
    # 打开PDF文件
    pdfFile = open(path, 'rb')

    # 创建pdf文档分析器
    parser = PDFParser(pdfFile)

    # 创建PDF文档对象存储文档结构
    document = PDFDocument(parser)

    # 检查文件是否允许文本提取
    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed

    # 创建PDF资源管理器对象来存储共享资源
    resource = PDFResourceManager()

    # 设定参数进行分析
    laparams = LAParams()

    # 创建一个PDF设备对象
    device = PDFPageAggregator(resource, laparams=laparams)

    # 创建一个PDF解释器对象
    interpreter = PDFPageInterpreter(resource,device)

    # 创建存储转换结果的同名txt文件
    fileName = str(path.split(".")[0])
    newFileName = fileName + ".txt"
    f = open(newFileName, "w")

    # 处理每一页
    for page in PDFPage.create_pages(document):
        interpreter.process_page(page)
        # 接受该页面的LTPage对象
        layout = device.get_result()
        for x in layout:
            if (isinstance(x, LTTextBoxHorizontal)):
                # 写入txt文件
                try:
                    f.writelines(x.get_text() + "\n")
                except:
                    pass
    f.close()

# 下载所有pdf文件的函数
def downloadpdf():
    pdfUrl = []  # 存放所有pdf文件的连接
    # 爬取所有的pdf文件的连接
    urlList = [
        "http://61.147.171.105:61770/",
        "http://61.147.171.105:61770/1/index.html",
        "http://61.147.171.105:61770/1/2/index.html",
        "http://61.147.171.105:61770/1/2/4/index.html",
        "http://61.147.171.105:61770/1/2/5/index.html",
        "http://61.147.171.105:61770/1/3/index.html",
        "http://61.147.171.105:61770/1/3/6/index.html",
        "http://61.147.171.105:61770/1/3/7/index.html",
        "http://61.147.171.105:61770/1/3/7/8/index.html"
        ]
    for each in urlList:
        r = requests.get(url=each)
        soup = BeautifulSoup(r.text, 'lxml')
        result = soup.find_all(name="a", attrs={"title":"my very fav paper"})
        for tmp in result:
            if tmp["href"].endswith(".pdf"):
                pdfUrl.append(each.split("index.html")[0] + tmp["href"])

    # 使用curl -O 命令下载pdf文件
    for each in pdfUrl:
        os.system("curl -O " + each)


# 取hash值的函数
def sha1(msg):
    sha1 = hashlib.sha1()
    sha1.update((msg + "Salz!").encode("utf-8"))
    return sha1.hexdigest()


# 破解密码的函数
def getpassword():
    passlist = {
        "3fab54a50e770d830c0416df817567662a9dc85c":"admin",
        "54eae8935c90f467427f05e4ece82cf569f89507":"fritze",
        "34b0bb7c304949f9ff2fc101eef0f048be10d3bd":"hansi"
    }
    for each in os.listdir(os.curdir):
        # 取出txt文件
        if each.endswith(".txt"):
            with open(each, "r") as file:
                a = file.read()
                b = re.split(r"[\s\,\;\.]+", a)  # 将单词分割出来
                c = []
                tmp = ""
                judge = False
                # 处理以-结尾的行，最终的结果保存在c中
                for each in b:
                    if each.endswith("-"):
                        tmp = each.split("-")[0]
                        judge = True
                    elif judge:
                        c.append(tmp + each)
                        judge = False
                    else:
                        c.append(each)
                # 遍历c碰撞得到密码
                for each in c:
                    print(each)
                    if sha1(each) in passlist:
                        return "----" + passlist[sha1(each)] + "'s password is " + each + "Salz!" + "----"


def main():
    os.chdir(os.curdir + os.sep + "pdfdir")  # 修改工作目录
    downloadpdf()  # 下载pdf文件

    # 将所有pdf文件转换成txt文件
    for each in os.listdir(os.curdir):
        pdf2txt(each)

    # 遍历所有的txt文件得到密码
    password = getpassword()
    return password


# if __name__ == "__main__":
#     print(main())

