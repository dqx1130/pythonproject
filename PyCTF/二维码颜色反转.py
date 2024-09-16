from PIL import Image
import numpy as np

img = Image.open('flag.png')  # 打开图片
matrix = 255 - np.asarray(img)  # 图像转矩阵 并反色
new_img = Image.fromarray(matrix)  # 矩阵转图像
new_img.save('flag_ok.png')  # 保存图片
