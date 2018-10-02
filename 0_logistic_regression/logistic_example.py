#良／恶性乳腺癌肿瘤预测

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# 根据官方数据构建类别
column_names = ['Sample code number','Clump Thickness','Uniformity of Cell Size','Uniformity of Cell Shape','Marginal Adhesion','Single Epithelial Cell Size','Bare Nuclei','Bland Chromatin','Normal Nucleoli','Mitoses','Class']

data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data',names = column_names)

# 将？替换成标准缺失值表示
data = data.replace(to_replace='?',value = np.nan)

# 丢弃带有缺失值的数据（只要一个维度有缺失）
data = data.dropna(how='any')

print("data.shape=", data.shape)

# 准备训练、测试数据集
X_train,X_test,y_train,y_test = train_test_split(data[column_names[1:10]],data[column_names[10]],test_size=0.25,random_state=42)

# 查看训练和测试样本的数量和类别分布
print('训练数据集的数量和样本分布')
print(y_train.value_counts())

print('测试数据集的数量和样本分布')
print(y_test.value_counts())

# 标准化数据，保证每个维度的特征数据方差为1，均值为0。使得预测结果不会被某些维度过大的特征值而主导
ss = StandardScaler()

X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

# 初始化 LogisticRegression
lr = LogisticRegression(C=1.0, penalty='l1', tol=0.01)

# 调用LogisticRegression中的fit函数／模块来训练模型参数
lr.fit(X_train,y_train)

lr_y_predict = lr.predict(X_test)

# 利用逻辑斯蒂回归自带的评分函数score获得模型在测试集上的准确定结果
print('精确率为：',lr.score(X_test,y_test))
print(classification_report(y_test,lr_y_predict,target_names = ['Benign','Maligant']))
