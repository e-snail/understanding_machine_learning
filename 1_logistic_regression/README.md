## Logistic Regression 逻辑回归/对数几率回归

Logistic Regression 被翻译成逻辑回归，也叫对数几率回归

#### 1. sklearn API

sklearn.linear_model.LogisticRegression 

参数说明: https://blog.csdn.net/jark_/article/details/78342644

#### 2. 练习

良／恶性乳腺癌肿瘤预测

logistic_example.py

#### 3. 对数几率回归 推导过程

Q1: 线性模型是解决回归问题的，如何应用到分类问题上？

Q2: 线性模型应用到二分类任务时使用的数学函数？

- 单位阶跃函数 unit-step function

Q3: 线性模型应用到多分类任务时使用的数学函数？

- 对数几率函数 logistic function

$$ y =\frac{1}{1 + e^{-z}} $$ (公式1)

$$ \ln  \frac{y}{1-y} = w^{T} + b $$  

Q4: 求解对数几率回归(公式1)的参数时为什么引入后验概率估计 ?

- 方便使用极大似然法(maximum likehood method)

Q5: 使用极大似然法来求解参数w/b的时候，为什么引入对数似然(log-likehood) ?

Q6: 以下等式的含义是什么？

$ L(w, b) = \sum_{i=1}^{m} ln \left (y_{i} | x_{i}; w, b \right ) $

- 这是对给定的数据集，其对率回归模型最大化"对数似然"（log-likehood）
- 直白含义就是每个样本属于其真实标记的概率和越大越好
- 等式右侧为什么加上ln ?
	- 这个显然是跟对数几率回归有关系，怎么详细解释？
- 等式右侧的 y|x;w,b 怎么解释？ 

Q7: 使用极大似然法来求解参数w/b的推导过程？

Q8: 计算对几率回归的目的是什么？ 也就是对几率回归的应用？

- 处理分类问题，预测给定的样本属于某个分类标签的概率，不是预测样本的标签值。
- [参考文章](https://www.cnblogs.com/JZ-Ser/articles/8474723.html)

