import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import os
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.datasets import load_iris
from sklearn.datasets import load_sample_image

# 简单的跑下tensorflow里的数据，看下效果
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

if __name__ == '__main__':
    # 读图片
    # iris = load_iris()  # 加载数据集
    # x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3)  # 划分训练集与测试集
    # clf = DecisionTreeClassifier()  # 采用决策树模型
    # clf.fit(x_train, y_train)  # 训练模型
    # predict_target = clf.predict(x_test)  # 加载测试集
    # print(sum(predict_target == y_test))  # 预测结果与真实结果比对
    # print(metrics.classification_report(y_test, predict_target))
    # print(metrics.confusion_matrix(y_test, predict_target))  # 输出混淆矩阵
    # L1 = [n[0] for n in x_test]
    # L2 = [n[1] for n in x_test]
    # plt.scatter(L1, L2, c=predict_target, marker='x')
    # plt.title('DecisionTreeClassifier')
    # plt.show()
    # iris = datasets.load_iris()  # 导入鸢尾花数据
    # print(iris.data.shape, iris.target.shape)  # (150, 4) (150,)
    # print(iris.feature_names)  # [花萼长，花萼宽，花瓣长，花瓣宽]

    # cnn神经网络
    china = load_sample_image('china.jpg') / 255
    flower = load_sample_image('flower.jpg') / 255
    images = np.array([china, flower])
    batch_sizes, height, width, channels = images.shape
    print(batch_sizes, height, width, channels)
    # 创建滤波器
    filters = np.zeros(shape=(7, 7, channels, 2))
    filters[:, 3, :, 0] = 10  # 将第三行弄成1
    filters[3, :, :, 1] = 1  # horizontal line

    outputs = tf.nn.conv2d(images, filters, strides=1, padding="SAME")
    print('out:', outputs[0, :, :, 1])
    plt.imshow(outputs[0, :, :, 1])
    plt.show()
