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
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.impute import SimpleImputer
from sklearn.linear_model import  LinearRegression
import matplotlib.pyplot as plt
#  引入公共方法
import sys

sys.path.append('..')
from common.utils import *

ssl._create_default_https_context = ssl._create_unverified_context

# 简单的跑下tensorflow里的数据，看下效果 加上这句的原因是python代码报错
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 设置变量值
DOWNLOAD_ROOT = "https://github.com/ageron/handson-ml2/tree/master/"
HOUSEING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

pr('HOUSING_URL', HOUSING_URL)


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
    # pr('housing.head()', housing.head())
    # pr('housing.info()', housing.info())
    # pr('housing value_counts', housing['ocean_proximity'].value_counts())
    # pr('housing.describe', housing.describe())
    # housing.hist(bins=50, figsize=(20, 15))
    # plt.show()
    #  直接选取测试集
    train_set, test_set = train_test_split(housing, test_size=0.3, random_state=42)
    # 分层选取测试集
    split = StratifiedShuffleSplit(n_splits=1, test_size=0.3, random_state=42)
    pr('hosusing', housing.info())
    housing["income_cat"] = pd.cut(housing["median_income"], bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
                                   labels=[1, 2, 3, 4, 5])
    housing["income_cat"].hist()

for train_index, test_index in split.split(housing, housing['income_cat']):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]
print('train_len', len(train_set), len(strat_train_set))
print('test_len', len(test_set), len(strat_test_set))
pr('strat_test_set', strat_train_set["income_cat"].value_counts() / len(strat_test_set))
housing = strat_train_set.copy()
housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4,
             s=housing["population"] / 100, label="population", figsize=(10, 7),
             c="median_house_value", cmap=plt.get_cmap('jet'), colorbar=True
             )
# plt.legend()
# plt.show()

corr_matrix = housing.corr()
# pr('corr_matrix', corr_matrix.info())
pr('corr_matrix', corr_matrix["median_house_value"].sort_values(ascending=False))

#   机器学习算法的准备
housing = strat_train_set.drop("median_house_value", axis=1)
housing_labels = strat_train_set["median_house_value"].copy()

# 数据清理有三种方法
'''
1. 放弃这些相应的区域
2. 放弃整个属性
3. 将缺失的值设置为某个值（0，平均数或者中位数等）
   通过dataframe的dropna(),drop()和fillna()方法，可以完成
'''
housing.dropna(subset=["total_bedrooms"])
housing.drop("total_bedrooms", axis=1)
median = housing['total_bedrooms'].median()
housing["total_bedrooms"].fillna(median, inplace=True)

'''
使用simpleimputer来代替缺失值
'''

imputer = SimpleImputer(strategy="median")
housing_num = housing.drop("ocean_proximity", axis=1)

imputer.fit(housing_num)
x = imputer.transform(housing_num)
pr('imputer',x)

'''
选择和训练模型，训练一个线性回归模型
'''
lin_reg = LinearRegression()
