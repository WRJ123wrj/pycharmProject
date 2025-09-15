from PIL import Image, ImageEnhance

# 打开图像，使用原始字符串或转义反斜杠的路径
img_original = Image.open(r"C:\Users\wrj\Desktop\系统开发工具基础\03-picture\001.jpg")
# 显示原始图像
img_original.show("原图")

# 创建对比度增强对象
img_enhancer = ImageEnhance.Contrast(img_original)
# 增强对比度，参数就是倍数
img = img_enhancer.enhance(3.0)
# 显示增强对比度后的图像
img.show("对比图")


