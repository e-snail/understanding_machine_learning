import numpy as np
from matplotlib import pyplot as plt

# 加载鸢尾花数据集
def load_dataset_flower():
    from sklearn import datasets
    iris = datasets.load_iris()
    # X_f = iris['data']
    # y_f = iris['target']
    # print('加载鸢尾花数据集成功：', iris)
    return iris

# softmax 回归多分类
def softmax_classify(iris):
    from sklearn.linear_model import LogisticRegression
    # 划分数据集
    X = iris["data"][:, (2, 3)]  # petal length, petal width
    y = iris["target"]
    # 创建 softmax 回归实例, 注意使用的参数
    softmax_reg = LogisticRegression(multi_class="multinomial", solver="lbfgs", C=10)
    softmax_reg.fit(X, y)
    # 预测
    predict = softmax_reg.predict([[5, 2]])
    predict_pro = softmax_reg.predict_proba([[5, 2]])
    print('softmax回归预测类型为：', predict)
    print('各类型的概率为', predict_pro)


if __name__ == '__main__':

    # 加载花的数据集
    iris = load_dataset_flower()

    # logistic 回归二分类
    # logistic_classify(iris)
    # softmax 多分类
    softmax_classify(iris)
