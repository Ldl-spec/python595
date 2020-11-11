## 什么是蒙特卡洛方法？

蒙特·卡罗方法（Monte Carlo method），也称统计模拟方法，是二十世纪四十年代中期由于科学技术的发展和电子计算机的发明，而被提出的一种以概率统计理论为指导的一类非常重要的数值计算方法。是指使用[随机数](https://baike.baidu.com/item/随机数/2454368)（或更常见的伪随机数）来解决很多计算问题的方法。

蒙特卡洛（Monte Carlo）方法是由大名鼎鼎的数学家冯·诺伊曼提出的，诞生于上世纪40年代美国的“曼哈顿计划”。原理是通过大量随机样本，去了解一个系统，进而得到所要计算的值。

## 通过蒙特卡洛方法计算圆周率π的原理

一个正方形内部相切一个圆，圆的面积是C，正方形的面积S，圆和正方形的面积之比是π/4。

![\frac{C}{S}=\frac{\pi r^2}{4r^2}=\frac{\pi}{4}\\](https://math.jianshu.com/math?formula=%5Cfrac%7BC%7D%7BS%7D%3D%5Cfrac%7B%5Cpi%20r%5E2%7D%7B4r%5E2%7D%3D%5Cfrac%7B%5Cpi%7D%7B4%7D%5C%5C)

![img](https:////upload-images.jianshu.io/upload_images/15946598-d1ff78290b757f97?imageMogr2/auto-orient/strip|imageView2/2/w/500)

image



在这个正方形内部，随机产生n个点（这些点服从均匀分布），计算它们与中心点的距离是否大于圆的半径，以此判断是否落在圆的内部。落在圆内部的点数统计出来是m个点。那么m、n点数个数的比例也符合面积的比：

![\frac{m}{n}=\frac{\pi}{4}\\](https://math.jianshu.com/math?formula=%5Cfrac%7Bm%7D%7Bn%7D%3D%5Cfrac%7B%5Cpi%7D%7B4%7D%5C%5C)

m与n的比值乘以4，就是π的值:

![{\pi}=\frac{m}{n}\cdot {4}](https://math.jianshu.com/math?formula=%7B%5Cpi%7D%3D%5Cfrac%7Bm%7D%7Bn%7D%5Ccdot%20%7B4%7D)

如果m、n足够大的话，那么就可以求出π的值。

## 代码实现

i是当前的次数，n是总的次数，count是在圆圈内的次数。



```python
import random
import math


def monte_carlo(n):
    i = 0
    count = 0
    while i <= n:
        x = random.random()
        y = random.random()
        if math.pow(x, 2) + math.pow(y, 2) < 1:
            count += 1
        i += 1
    pi = 4*count/n
    print(pi)


monte_carlo(10000000)
```

上面的代码我们要注意这么几点：

pow() 通过内置的方法直接调用，内置方法会把参数作为整型，而 math 模块则会把参数转换为 float。

## 蒙特卡洛求定积分

蒙特卡洛方法的一个重要应用就是求定积分。来看下面的一个例子

![img](https:////upload-images.jianshu.io/upload_images/15946598-7c1f451796aa9936?imageMogr2/auto-orient/strip|imageView2/2/w/676)

img

当我们在[a,b]之间随机取一点x时，它对应的函数值就是f(x)。接下来我们就可以用f(x) * (b - a)来粗略估计曲线下方的面积，也就是我们需要求的积分值，当然这种估计（或近似）是非常粗略的。

![img](https:////upload-images.jianshu.io/upload_images/15946598-e045c32172987936?imageMogr2/auto-orient/strip|imageView2/2/w/670)

img

在此图中，做了四次随机采样，得到了四个随机样本x1,x2,x3,x4，并且得到了这四个样本的f(xi)的值分别为f(x1),f(x2),f(x3),f(x4)。对于这四个样本，每个样本能求一个近似的面积值，大小为f(xi)∗(b−a)。为什么能这么干么？对照图下面那部分很容易理解，每个样本都是对原函数f的近似，所以我们认为f(x)的值一直都等于f(xi)

按照图中的提示，求出上述面积的数学期望，就完成了蒙特卡洛积分。

如果用数学公式表达上述过程：
![\begin{align} S &\approx \frac{1}{4}(f(x_{1})(b-a)+f(x_{2})(b-a)+f(x_{3})(b-a)+f(x_{4})(b-a))\\ &\approx \frac{1}{4}(b-a)(f(x_{1})+f(x_{2})+f(x_{3})+f(x_{4}))\\ &\approx \frac{1}{4}(b-a)\sum _{i=1}^{4}f(x_{i}) \end{align}](https://math.jianshu.com/math?formula=%5Cbegin%7Balign%7D%20S%20%26%5Capprox%20%5Cfrac%7B1%7D%7B4%7D(f(x_%7B1%7D)(b-a)%2Bf(x_%7B2%7D)(b-a)%2Bf(x_%7B3%7D)(b-a)%2Bf(x_%7B4%7D)(b-a))%5C%5C%20%26%5Capprox%20%5Cfrac%7B1%7D%7B4%7D(b-a)(f(x_%7B1%7D)%2Bf(x_%7B2%7D)%2Bf(x_%7B3%7D)%2Bf(x_%7B4%7D))%5C%5C%20%26%5Capprox%20%5Cfrac%7B1%7D%7B4%7D(b-a)%5Csum%20_%7Bi%3D1%7D%5E%7B4%7Df(x_%7Bi%7D)%20%5Cend%7Balign%7D)
对于更一般的情况，假设要计算的积分如下：
![I = \int_{a}^{b}g(x)dx](https://math.jianshu.com/math?formula=I%20%3D%20%5Cint_%7Ba%7D%5E%7Bb%7Dg(x)dx)
其中被积函数g(x)在[a,b)内可积，如果选择一个概率密度函数为![f_{X}(x)](https://math.jianshu.com/math?formula=f_%7BX%7D(x))的方式进行抽样，而且满足![\int_{a}^{b}f_{X}(x)dx=1](https://math.jianshu.com/math?formula=%5Cint_%7Ba%7D%5E%7Bb%7Df_%7BX%7D(x)dx%3D1)，那么令![g^*(x)=\frac{g(x)}{f_{X}(x)}](https://math.jianshu.com/math?formula=g%5E*(x)%3D%5Cfrac%7Bg(x)%7D%7Bf_%7BX%7D(x)%7D)，原有的积分可以写成下面的形式：
![I = \int_{a}^{b}g^*(x)f_{X}(x)dx](https://math.jianshu.com/math?formula=I%20%3D%20%5Cint_%7Ba%7D%5E%7Bb%7Dg%5E*(x)f_%7BX%7D(x)dx)

那么我们求积分的步骤应该是：

1.产生服从分布律![F_{X}](https://math.jianshu.com/math?formula=F_%7BX%7D)的随机变量![X_{i}](https://math.jianshu.com/math?formula=X_%7Bi%7D)(i=1,2,⋯,N)

2.计算均值
![\bar{I}=\frac{1}{N}\sum_{i=1}^{N}g^*(X_i)](https://math.jianshu.com/math?formula=%5Cbar%7BI%7D%3D%5Cfrac%7B1%7D%7BN%7D%5Csum_%7Bi%3D1%7D%5E%7BN%7Dg%5E*(X_i))
这个时候有：
![\bar I \approx I](https://math.jianshu.com/math?formula=%5Cbar%20I%20%5Capprox%20I)
当然实际应用中，我们最常用的还是取![f_{X}](https://math.jianshu.com/math?formula=f_%7BX%7D)为均匀分布：

![f_{X}(x)=\frac{1}{b-a},a\leq x \leq b](https://math.jianshu.com/math?formula=f_%7BX%7D(x)%3D%5Cfrac%7B1%7D%7Bb-a%7D%2Ca%5Cleq%20x%20%5Cleq%20b)
此时：
![g^{*}(x)=(b-a)g(x)](https://math.jianshu.com/math?formula=g%5E%7B*%7D(x)%3D(b-a)g(x))
带入积分表达式I:


![I = （b-a）\int_{a}^{b}g(x)\frac{1}{b-a}dx](https://math.jianshu.com/math?formula=I%20%3D%20%EF%BC%88b-a%EF%BC%89%5Cint_%7Ba%7D%5E%7Bb%7Dg(x)%5Cfrac%7B1%7D%7Bb-a%7Ddx)
最后有：

![\bar I = \frac{b-a}{N}\sum_{i=1}^{N}g(X_{i})](https://math.jianshu.com/math?formula=%5Cbar%20I%20%3D%20%5Cfrac%7Bb-a%7D%7BN%7D%5Csum_%7Bi%3D1%7D%5E%7BN%7Dg(X_%7Bi%7D))

如果从直观上理解这个式子也非常简洁明了：
在[a,b)区间上按均匀分布取N个随机样本![X_{i}](https://math.jianshu.com/math?formula=X_%7Bi%7D),计算![g(X_i)](https://math.jianshu.com/math?formula=g(X_i))并取均值，得到的相当于Y坐标值，然后乘以(b−a)为X坐标长度，得到的即为对应矩形的面积，即积分值。

## 代码实现

假设我们想求的积分值![\int_{0}^{1}x^{2}dx](https://math.jianshu.com/math?formula=%5Cint_%7B0%7D%5E%7B1%7Dx%5E%7B2%7Ddx)



```python
import random


def integral():
    n = 1000000
    count = 0

    x_min, x_max = 0.0, 1.0
    y_min, y_max = 0.0, 1.0

    for i in range(0, n):
        x = random.uniform(x_min, x_max)
        y = random.uniform(y_min, y_max)

        if x*x > y:
            count += 1

    integral_value = count / float(n)
    print(integral_value)


integral()
```

请注意if x*x > y:这句话中

x * x 是表示原本函数的值，也就是曲线的位置

y是自己的随机点生成的位置。



作者：等等_88e2
链接：https://www.jianshu.com/p/7e64651ff82d
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。