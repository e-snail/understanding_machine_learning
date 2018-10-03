## Logistic Regression 逻辑回归

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

$$ y =\frac{1}{1 + e^{-z}} $$

==>

\ln  \frac{y}{1-y} = w^{T} + b

 


