# Matplotlib教程
## 参考资料
1. [Matplotlib 入门教程](https://www.gitbook.com/book/wizardforcel/matplotlib-intro-tut/details)
## Matplotlib简介
## [pylab和pyplot的区别](https://www.cnblogs.com/Shoesy/p/6673947.html)
查阅网上资料，对Pyplot的解说：“方便快速绘图matplotlib通过pyplot模块提供了一套和MATLAB类似的绘图API，将众多绘图对象所构成的复杂结构隐藏在这套API内部。”

对pylab的解说：“matplotlib还提供了一个名为pylab的模块，其中包括了许多NumPy和pyplot模块中常用的函数，方便用户快速进行计算和绘图，十分适合在IPython交互式环境中使用。”

对比原文注释(pylab combines pyplot with numpy into a single namespace. This is convenient for interactive work, but for programming it is recommended that the namespaces be kept separate)意思就是说pylab结合了pyplot和numpy，对交互式使用来说比较方便，既可以画图又可以进行简单的计算。但是，对于一个项目来说，建议分别倒入使用，即：

import numpy as np

import matplotlib.pyplot as plt

而不是

import pylab as pl

## 函数式使用——pyplot
matplotlib.pyplot是一个有命令风格的函数集合，它看起来和MATLAB很相似。**每一个pyplot函数都使一副图像做出些许改变**，例如创建一幅图，在图中创建一个绘图区域，在绘图区域中添加一条线等等。在matplotlib.pyplot中，各种状态通过函数调用保存起来，以便于可以随时跟踪像当前图像和绘图区域这样的东西。绘图函数是直接作用于当前axes（matplotlib中的专有名词，图形中组成部分，不是数学中的坐标系。）
### 基本使用
1. 导入包
```py
import matplotlib.pyplot as plt
```
1. 后台绘制
```py
plt.plot([1,2,3],[5,7,4])
```
1. 显示到屏幕
```py
plt.show()
```
### 图例、标题和标签

```py
#  -*- coding:utf8 -*-
import matplotlib.pyplot as plt
x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,12]

plt.plot(x, y, label='First Line')
plt.plot(x2, y2, label='Second Line')

plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Interesting Graph\nCheck it out')
# plt.legend() plt.show()
```
1. `lable`为每个线条指定名称
1. `xlable`、`ylabel`为x、y轴创建标签
1. `title`创建图的标题
1. `legend`生成默认图例
结果图如下：

![](https://pythonprogramming.net/static/images/matplotlib/titles-labels-legends-matplotlib.png)

### 条形图和直方图
#### 条形图
```python
import matplotlib.pyplot as plt
plt.bar([1,3,5,7,9],[5,2,7,8,2], label="Example one")
plt.bar([2,4,6,8,10],[8,6,2,5,6], label="Example two", color='g')

plt.legend()

plt.xlabel('bar number')
plt.ylabel('bar height')

plt.title('Epic Graph\nAnother Line! Whoa')

plt.show()
```
1. `plt.bar`为我们创建条形图
1. Matplotlib可以在任何类型的绘图中使用颜色，例如`g`为绿色，`b`为蓝色，`r`为红色，等等。还可以使用十六进制颜色代码，如`#191970`。

#### 直方图
直方图以区间形式显示一组数据，如下所示：
```python
import matplotlib.pyplot as plt

population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130] 

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8) 

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()

plt.show()
```
![](https://pythonprogramming.net/static/images/matplotlib/matplotlib-histogram-tutorial.png)

#### 其他
matplotlib还能绘制散点图、堆叠图、饼图等
[见链接](https://wizardforcel.gitbooks.io/matplotlib-intro-tut/content/matplotlib/4.html)


