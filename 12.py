from PIL import Image
import numpy as np

# 打开图像并转换为 NumPy 数组
img = np.array(Image.open(r"C:\Users\wrj\Desktop\系统开发工具基础\03-picture\001.jpg"))

# 分离并处理 RGB 通道
# 处理红色通道：将绿、蓝通道置 0
img_red = img.copy()
img_red[:, :, (1, 2)] = 0
# 处理绿色通道：将红、蓝通道置 0
img_green = img.copy()
img_green[:, :, (0, 2)] = 0
# 处理蓝色通道：将红、绿通道置 0
img_blue = img.copy()
img_blue[:, :, (0, 1)] = 0

# 拼接原图和三个单通道图，便于对比展示
img_rgb = np.concatenate((img, img_red, img_green, img_blue), axis=1)

# 将 NumPy 数组转回图像并显示
Image.fromarray(img_rgb).show()