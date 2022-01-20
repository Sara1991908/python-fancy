'''
   这个函数主要用于拉全程数据同时解析远程数据到本地文件夹
   然后进行读取
'''
from sklearn.datasets import fetch_openml

import os
import tarfile
import urllib
import urllib.request
# 加上下面这句的原因是发现是因为SSL 证书的验证问题
import ssl
from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier

#  引入公共方法
import sys

sys.path.append('..')
from common.utils import *

ssl._create_default_https_context = ssl._create_unverified_context

# 简单的跑下tensorflow里的数据，看下效果 加上这句的原因是python代码报错
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

if __name__ == '__main__':
    mnist = fetch_openml('data')
    pr('mist', mnist.keys())
    x, y = mnist["data"], mnist["target"]
    # some_digit_image = some_digit.reshape(28, 28)
    print('x.shape', getType(x))

    # plt.imshow(image_file, cmap="binary")
    # plt.zxis('off')
    # plt.show()
    # x_train, x_test, y_train, y_test = x[:60000], x[60000:], y[:60000], y[60000:]
    # sgd_clf = SGDClassifier(random_state=42)
    # y_train_5 = (y_train == 5)
    # sgd_clf.fit(x_train, y_train_5)
