import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import seaborn

import tensorflow as tf
import os

if __name__ == '__main__':
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    tf.compat.v1.disable_eager_execution()
hello = tf.constant('hello,tensorflow')
sess = tf.compat.v1.Session()
print(sess.run(hello))
