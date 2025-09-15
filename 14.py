import cv2
# 读取图像
img = cv2.imread(r"C:\Users\wrj\Desktop\系统开发工具基础\03-picture\003.jpg")
# 裁剪图像：截取从行 50 到 283，列 25 到 190 的区域
img_cropped = img[0:540, 0:540]
# 获取裁剪后图像的形状（行数、列数、通道数）
shape = img_cropped.shape

# 打印裁剪后图像的行数
print(shape[0])
# 缩放图像：将裁剪后的图像高度变为原来的 12/10 倍，宽度变为原来的 1.5 倍
img_cropped_resized = cv2.resize(img_cropped, (int(shape[1] * 1.5), int(shape[0] * 12 / 10)))

#显示裁剪后的图像
cv2.imshow("Red Flower",img_cropped)
# 显示裁剪并缩放后的图像
cv2.imshow("Image cropped", img_cropped_resized)
# 显示原始图像
cv2.imshow("Image", img)

# 等待键盘输入，按下任意键后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()