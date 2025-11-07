import binascii

hex_data='txt文件中16进制数据'
out=open('flag.rar','wb')
out.write(binascii.unhexlify(hex_data))
out.close()

