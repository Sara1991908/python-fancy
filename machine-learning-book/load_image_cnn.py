import sklearn.datasets as load_image_cnn
import numpy as np

if __name__ != '__main__':
    # 读图片
    china = load_image_cnn('china.jpg') / 255
    flower = load_image_cnn('flower.jpg') / 255
    images = np.array([china, flower])
    batch_sizes, height, width, channels = images.shape

    # 创建滤波器
