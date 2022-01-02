import tensorflow.compat.v1 as tf
import os
import _pickle as cPickle
import numpy as np

tf.compat.v1.disable_eager_execution()


def load_data(filename):
    with open(filename, 'rb') as f:
        data = cPickle.load(f)
        return data['data'], data['labels']


if __name__ == '__main__':
    CIFAR_DIR = "../../imooc/cifar-10-batches-py"
    print(os.listdir(CIFAR_DIR))
x = tf.placeholder(tf.float32, [None, 3072])
y = tf.placeholder(tf.int64, [None])
w = tf.get_variable('w', [x.get_shape()[-1], 1], initializer=tf.random_normal_initializer(0, 1))
b = tf.get_variable('b', [1], initializer=tf.constant_initializer(0.0))
print(w, y, w, b)

# y是神经元函数
y_ = tf.matmul(x, w) + b
p_y_1 = tf.nn.sigmoid(y_)
y_reshaped = tf.reshape(y, (-1, 1))
y_reshaped_float = tf.cast(y_reshaped, tf.float32)
# 用均值函数计算损失函数
loss = tf.reduce_mean(tf.square(y_reshaped_float - p_y_1))

# bool
predict = p_y_1 > 0.5
correct_prediction = tf.equal(tf.cast(predict, tf.int64), y_reshaped)
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float64))
