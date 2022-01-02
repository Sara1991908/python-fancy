import sklearn.datasets as load_image_cnn
import numpy as np
import plotlib as plt

if __name__ == '__main__':
    # 读图片
    china = load_image_cnn('china.jpg') / 255
    flower = load_image_cnn('flower.jpg') / 255
    images = np.array([china, flower])
    batch_sizes, height, width, channels = images.shape
    print(batch_sizes, height, width, channels)
    # 创建滤波器
    filters = np.zeros(shape=(7, 7, channels, 2))
    fiters[:, 3, :, 0] = 1  # 将第三行弄成1
    fitters[3, :, :, 1] = 1  # horizontal line

    outputs = tf.cnn.conv2d(images, filters, strides=1, padding="same")
    plt.imshow(outputs[0, :, :1], cmap="gray")
    plt.show()
