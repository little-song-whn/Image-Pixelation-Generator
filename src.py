from PIL import Image
import matplotlib.pyplot as plt

def pixelate(img_path, pixel_size=10, num_colors=16, save_path="example.png"):
    """
    读取图片并转换成像素风格
    :param img_path: 图片路径
    :param pixel_size: 像素大小（越大，像素化程度越高）
    :param num_colors: 颜色种类数（越少，越接近复古像素风格）
    :param save_path: 保存路径
    """
    # 读取原图
    img = Image.open(img_path)
    
    # 获取原始尺寸
    width, height = img.size
    
    # 1️ **降低分辨率（像素化）**
    img_small = img.resize((width // pixel_size, height // pixel_size), Image.Resampling.BILINEAR)
    img_pixelated = img_small.resize((width, height), Image.Resampling.NEAREST)
    
    # 2️ **颜色量化**
    img_quantized = img_pixelated.convert("P", palette=Image.ADAPTIVE, colors=num_colors).convert("RGB")

    # 显示最终效果
    plt.imshow(img_quantized)
    plt.axis("off")
    plt.show()

    # 3️ **保存像素画**
    img_quantized.save(save_path)
    print(f"已保存像素画：{save_path}")

pixelate("C:/Users/25771/OneDrive/桌面/新建文件夹/example2.png", pixel_size=15, num_colors=8, save_path="pixel_art_output.png")
