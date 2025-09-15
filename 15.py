from wand.image import Image
import os
import subprocess

def apply_image_effects():
    input_path = r"C:\Users\wrj\Desktop\系统开发工具基础\03-picture\004.jpg"

    if not os.path.exists(input_path):
        print(f"错误：找不到文件 {input_path}")
        return
    # 打开原始图像
    with Image(filename=input_path) as img:
        # 浮雕效果
        with img.clone() as embossed:
            embossed.emboss(radius=4, sigma=6)
            embossed.save(filename='004-1.jpg')
            print("已保存浮雕效果：004-1.jpg")
        # 油画效果
        with img.clone() as painted:
            painted.oil_paint(radius=8)
            painted.save(filename='004-2.jpg')
            print("已保存油画效果：004-2.jpg")
apply_image_effects()