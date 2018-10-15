## Decision Tree 决策树

核心问题：
- 如何构建一颗决策树？
- 构建决策树的依据是什么？

### 2. 构建一棵树决策树的过程

名词：
- 训练集
- 属性集
- 分支结点：代表数据/样本的类别

构建过程：

通过一个递归函数来为每个结点找到最合适属性集，直到结束条件出现：
- 所有节点都属于同一属性类型，无需划分

### 2.1 构建决策树的核心问题

选择最优划分属性，也就是让分支结点所包含的样本尽可能属于同一类，即结点的“纯度”高。

通俗的理解最优属性就是包含最多样本的属性，每次都选择这样的属性，就能最先把尽量多的样本分类出去。

这样做是不是太简单了？数学家们肯定不会用这么low的办法。于是，他们搞出了个“信息增益”的概念。

某个属性的"信息增益"越大，就应该首先使用它来作为决策树的结点。

先了解信息熵的概念。

#### 2.1.1 信息熵Information Entropy

怎么量化“纯度” ？

信息熵定义描述：假定当前集合D中第k类样本所占的比例为
![](http://latex.codecogs.com/png.latex?p_{k})k=1,2,...,|y|, 则D的信息熵定义为:

![](http://latex.codecogs.com/png.latex?Ent(D)=-\sum_{k=1}^{|y|}p_{k}log_{2}^{p_{k}})

注意：
- 这是计算集合D的信息熵
- |y|代表的是集合D的元素类别个数, 注意不是元素个数
- 为什么要给连加号前加个负号？
  - ![](http://latex.codecogs.com/png.latex?p_{k})必定小于或等于1,所以![](http://latex.codecogs.com/png.latex?log_{2}^{k})必定小于或等于0.
  - 为了让Ent(D)大于0就加上了负号.
- Ent(D)的极值
  - 最小值 0: 当![](http://latex.codecogs.com/png.latex?p_{k})等于0时
  - 最大值 ![](http://latex.codecogs.com/png.latex?log_{2}^{|y|})
    - 条件是所有集合D中所有类别的样本数量相等，也就是说![](http://latex.codecogs.com/png.latex?p_{k})等于1/|y|.
    - 取最大值的意义是：D中所有类别包含的样本数量一样多，这种情况样本混合度最高，纯度也是最小


#### 2.1.2 信息增益Information Gain

信息增益的定义:

![](http://latex.codecogs.com/png.latex?Gain(D,a)=Ent(D)-\sum_{v=1}^{V}\frac{|D^{v}|}{|D|}Ent(D^{v}))

参数说明:
- a是离散属性
- a属性包含V个可能的取值![](http://latex.codecogs.com/png.latex?{a^{1},a^{2},...,a^{V}}) 例如：颜色属性可能的取值为{红色, 绿色, ...}
- r 如果使用属性a 对样本集进行划分， 就会产生V个分支结点， 其中第v个分支结点包含了 ![](http://latex.codecogs.com/png.latex?D^{v}) 个 样本，这些样本的属性取值都是![](http://latex.codecogs.com/png.latex?{a^{v}})
- ![](http://latex.codecogs.com/png.latex?|D^{v}|)是D中包含分类为a的第v类属性的样本数量
- ![](http://latex.codecogs.com/png.latex?Ent(D^{v}))的意义是计算样本![](http://latex.codecogs.com/png.latex?D^{v})的信息熵，此时信息熵公式中的|y|=1，就是说只有一类样本

意义说明:
- 这是求属性a的信息增益
- 信息增益越大, 意味着使用属性a来划分样本所获得的"纯度提升"越大


#### 2.1.3 以西瓜数据集为例来构建决策树

- 信息熵公式中|y|=2，意思是西瓜分类只有好瓜和坏瓜两种
- 计算出好瓜和坏瓜的数量就可以计算出Ent(D)
