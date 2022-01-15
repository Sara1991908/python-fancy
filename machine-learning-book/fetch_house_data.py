'''
   这个函数主要用于拉全程数据同时解析远程数据到本地文件夹
   然后进行读取
'''
import os
import tarfile
import urllib
import urllib.request
# 加上下面这句的原因是发现是因为SSL 证书的验证问题
import ssl
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context

# 简单的跑下tensorflow里的数据，看下效果 加上这句的原因是python代码报错
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 设置变量值
DOWNLOAD_ROOT = "https://github.com/ageron/handson-ml2/tree/master/"
HOUSEING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

print('HOUSING_URL', HOUSING_URL)


def fetch_housing_data(houseing_url=HOUSING_URL, housing_path=HOUSEING_PATH):
    # os.makedirs(housing_path, exist_ok=True)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    # print('tgz_path', tgz_path)
    # urllib.request.urlretrieve(houseing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)

    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()


def load_housing_data(housing_path=HOUSEING_PATH):
    csv_path = os.path.join(housing_path, 'housing.csv')
    return pd.read_csv(csv_path)


if __name__ == '__main__':
    fetch_housing_data()
    housing = load_housing_data()
    print('housing.head:\n ', housing.head(), '\n', housing.info())
