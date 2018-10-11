## Logistic Regression 逻辑回归/对数几率回归

Logistic Regression 被翻译成逻辑回归，也叫对数几率回归

#### 1. sklearn API

sklearn.linear_model.LogisticRegression

参数说明: https://blog.csdn.net/jark_/article/details/78342644

#### 2. 练习

##### 练习1: 良／恶性乳腺癌肿瘤预测

源码: logistic_example.py

##### 练习2: 鸢尾花分类预测(softmax)

数据说明:

http://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
https://gist.github.com/curran/a08a1080b88344b0c8a7

源码: plot_iris_dataset.py

使用: sklearn.linear_model.LogisticRegression 的方法

创建softmax

```
# 参数说明，参考下一部分
softmax_reg = LogisticRegression(multi_class="multinomial", solver="lbfgs", C=10)

# predict() 用于预测
predict = softmax_reg.predict([[5, 2]])

# predict_proba 用户输出分类概率
predict_pro = softmax_reg.predict_proba([[5, 2]])

```

#### 3. LR的参数说明

LR 函数的所有参数

http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

- multi_class :
	- 分类方式的选择，有ovr和multinomial两个值可以选择，默认是 ovr。
		- ovr即前面提到的one-vs-rest(OvR)，而multinomial即前面提到的many-vs-many(MvM)。
		- 如果是二元逻辑回归，ovr和multinomial并没有任何区别，区别主要在多元逻辑回归上。
- solver：
	- 对逻辑回归损失函数的优化方法，有4种算法可以选择，分别是：
		- liblinear：使用了开源的liblinear库实现，内部使用了坐标轴下降法来迭代优化损失函数。
		- lbfgs：拟牛顿法的一种，利用损失函数二阶导数矩阵即海森矩阵来迭代优化损失函数。
		- newton-cg：也是牛顿法家族的一种，利用损失函数二阶导数矩阵即海森矩阵来迭代优化损失函数。
		- sag：即随机平均梯度下降，是梯度下降法的变种，和普通梯度下降法的区别是每次迭代仅仅用一部分的样本来计算梯度，适合于样本数据多的时候，SAG是一种线性收敛算法，这个速度远比SGD快。关于SAG的理解，参考博文线性收敛的随机优化算法之 SAG、SVRG（随机梯度下降）
- C
	- 正则化参数

#### 4. 对数几率回归 推导过程

Q1: 线性模型是解决回归问题的，如何应用到分类问题上？

Q2: 线性模型应用到二分类任务时使用的数学函数？

- 单位阶跃函数 unit-step function

Q3: 线性模型应用到多分类任务时使用的数学函数？

- 对数几率函数 logistic function


![](http://latex.codecogs.com/png.latex?y=\frac{1}{1+e^{-z}})

(公式1)

![](http://latex.codecogs.com/png.latex?ln\frac{y}{1-y}=w^{T}+b)

Q4: 求解对数几率回归(公式1)的参数时为什么引入后验概率估计 ?

- 方便使用极大似然法(maximum likehood method)

Q5: 使用极大似然法来求解参数w/b的时候，为什么引入对数似然(log-likehood) ?

- 看Q6

Q6: 以下等式的含义是什么？

\[
L(w, b)=\sum_{i=1}^{m}ln\left(y_{i}|x_{i};w,b\right)
\]

![](http://latex.codecogs.com/png.latex?l(w, b)=\sum_{i=1}^{m}ln\left(y_{i}|x_{i};w,b\right))


- 这是对给定的数据集，其对率回归模型最大化"对数似然"（log-likehood）
- 直白含义就是每个样本属于其真实标记的概率和越大越好
- 等式右侧为什么加上ln ?
	- 为了把连乘编程连加（看极大似然法发定义，其中是连乘）
	- 方便求导(连乘式中的参数要逐个求导，对连加式求导可以只考虑连加后边的符号)
	- 防止数据下溢, 就是我们的计算机的小数点是有限制的，如果很小的数一直相乘，可能会突破这个限制，就会报错
- 等式右侧的 y|x;w,b 怎么解释？
	- 主要是解释分号: 代表分布参数（比如均值、方差等等），也可以理解为在参数w/b条件下的y的概率

Q7: 使用极大似然法来求解参数w/b的推导过程？

Q8: 计算对几率回归的目的是什么？ 也就是对几率回归的应用？

- 处理分类问题，预测给定的样本属于某个分类标签的概率，不是预测样本的标签值。
- [参考文章](https://www.cnblogs.com/JZ-Ser/articles/8474723.html)
