
## 支持向量机SVM(Support Vector Merchines)

#### 基本概念

- 线性可分(linearly separable)
  - 如果存在一条直线将二维数据集划分成两组(不同分类)，那么这组数据被称为线性可分
- 分割超平面(separating hyperplane)
  - 线性可分中数据是二维的，如果将数据扩展到N维，能划分该数据集的必然是一个N-1维的平面, 该平面被称为分割超平面
  - 或者说，如果数据从N维退化成二维，那么分割超平面会退化成一条直线
- 支持向量
  - 训练集中, 距离超平面最近的几个向量
- 间隔 Margin
  - 我们希望支持向量到超平面的距离越大越好，这个距离被称为间隔


#### 核心问题: 计算最大间隔

`放弃这一章的公式推导，太难了`

分割超平面的数学表达式: ![](http://latex.codecogs.com/png.latex?w^{T}x+b)

点A到超平面的距离: ![](http://latex.codecogs.com/png.latex?\frac{|w^{T}x+b|}{||w||})
- ![](http://latex.codecogs.com/png.latex?|w^{T}x+b|)表示什么?
- ![](http://latex.codecogs.com/png.latex?||w||)什么含义 ?

假设超平面(w,b)能将训练样本正确分类，即对于某个样本点来说,如果分类为正例(y=+1), 则有![](http://latex.codecogs.com/png.latex?w^{T}x+b>0)，反例(y=-1)，则有![](http://latex.codecogs.com/png.latex?w^{T}x+b<0)，即有以下表达式

![](http://latex.codecogs.com/png.latex?\left(x_{i},y_{i} \right)\in D), 如果

![](http://latex.codecogs.com/png.latex?\underset{w,b}{max} \frac{2}{||w||})

这公式不知道为什么显示不出来....

通过朗格拉日乘子法将问题转换为另一个对偶问题

-------------------------------------------------
以下是《机器学习实战》中的部分内容，没能完全理解，先忽略

================


超平面代表一个分类器，`求解分类器中的w和b是关键`。问题转换为求以下数学表达式：

![](http://latex.codecogs.com/png.latex?\arg\underset{w,b}{max}\left\\{\underset{n}{min}\left(label\cdot\left(w^{T}+b\right)\right)\cdot\fracåå{1}{||w||}\right\\})

解释:
- 目标: 找到具有最小间隔的数据点(支持向量)，再对数据点与超平面的间隔最大化.
- ![](http://latex.codecogs.com/png.latex?\arg\underset{w,b}{max}) 间隔最大化条件下求w和b的值
- label: 数据集的分类标签，这里取值为{-1, 1}, 这是个取巧的做法，稍后解释
- 大括号内的表达式: 找到具有最小间隔的数据点

如何求解以上表达式 ?

分析得出该表达式的求解问题，是一个有约束条件的求最优值的问题。约束条件就是![](http://latex.codecogs.com/png.latex?label*(w^{T}+b)\geq1.0).

问题转化为:

公式太复杂....  先不写了

================

以上是《机器学习实战》中的部分内容，没能完全理解，先忽略

-------------------------------------------------
