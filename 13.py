import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from PIL import Image

image_path = r"C:\Users\wrj\Desktop\系统开发工具基础\03-picture\001.jpg"
img = Image.open(image_path).convert('L')  # 转换为灰度图像以便简化处理
img_array = np.array(img)  # 转换为numpy数组

# 应用高斯模糊（sigma值越大，模糊程度越高）
blurred_img = ndimage.gaussian_filter(img_array, sigma=5)

# 创建画布展示原图和处理后的图像
plt.figure(figsize=(10, 5))

# 显示原图
plt.subplot(1, 2, 1)
plt.imshow(img_array, cmap='gray')
plt.title('原图')
plt.axis('off')  # 隐藏坐标轴

# 显示模糊后的图像
plt.subplot(1, 2, 2)
plt.imshow(blurred_img, cmap='gray')
plt.title('高斯模糊处理后')
plt.axis('off')

# 展示图像
plt.tight_layout()
plt.show()
