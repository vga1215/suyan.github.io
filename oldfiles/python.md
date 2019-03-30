---
layout: docs
title:  Learn Python
prev_section: w3c
next_section:   
permalink: /docs/python/
---

###Python代码书写标准样式指导###

[PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

[web.py开发](http://my.oschina.net/zhengnazhi/blog/120332)

[Pyton2.7教程](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000)

--------------------
## Learn Python The Hard Way Notes:

Exercise 13中谈到**Parameters**（形参）和**arguments**(实参）区别：

>**Note:**

> - parameter:形参，指的是函数中的参数名称：

> - def add(x,y):>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>此处x,y为形参。
> - return x+y
 
> - argument:实参，指的是你提供给函数调用的值：

> - x=1
> - y=2
> - add(x,y)>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>此处x,y就变为实参了。

~~~
清单 5. 使用 yield 的第四版

 def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b 
        # print b 
        a, b = b, a + b 
        n = n + 1 

'''

第四个版本的 fab 和第一版相比，仅仅把 print b 改为了 yield b，就在保持简洁性的同时获得了 iterable 的效果。

调用第四版的 fab 和第二版的 fab 完全一致：

 >>> for n in fab(5): 
 ...     print n 
 ... 
 1 
 1 
 2 
 3 
 5

简单地讲，yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator，调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象！在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，执行到 yield b 时，fab 函数就返回一个迭代值，下次迭代时，代码从 yield b 的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到 yield。

也可以手动调用 fab(5) 的 next() 方法（因为 fab(5) 是一个 generator 对象，该对象具有 next() 方法），这样我们就可以更清楚地看到 fab 的执行流程：

~~~

###Python中的传值和引用###


n不允许程序员选择采用传值还是传引用。Python参数传递采用的肯定是“传对象引用”的方式。实际上，这种方式相当于传值和传引用的一种综合。如果函数收到的是一个可变对象（比如字典或者列表）的引用，就能修改对象的原始值－－相当于通过“传引用”来传递对象。如果函数收到的是一个不可变对象（比如*数字*、*字符*或者*元组*）的引用，就不能直接修改原始对象－－相当于通过“传值'来传递对象。

python一般内部赋值变量的话，都是传个引用变量，和C语言的传地址的概念差不多。可以用id()来查询内存地址

如果a=b的话， a和b的地址是相同的；如果只是想拷贝，那么就得用 a=b[:]。

！！！注意这一点，这可是可以引起重大错误的。。。

### python pip包管理###

  pip 是一个安装和管理 Python 包的工具 , 是 easy_install 的一个替换品。本文将详细说明 安装 pip 的方法和 使用 pip 的一些基本操作如安装、更新和卸载 python 包。

distribute是setuptools的取代(Setuptools包后期不再维护了)，pip是easy_install的取代。

pip的安装需要setuptools 或者 distribute，如果你使用的是Python3.x那么就只能使用distribute因为Python3.x不支持setuptools。

#wget http://python-distribute.org/distribute_setup.py

#python distribute_setup.py


setuptools安装:

#https://pypi.python.org/packages/source/s/setuptools/

#wget --no-check-certificate https://pypi.python.org/packages/source/s/setuptools/setuptools-1.4.2.tar.gz

#tar zxvf setuptools-1.4.2.tar.gz

#cd setuptools-1.4.2;python setup.py install;easy_install --version


安装Pip：

wget --no-check-certificate https://pypi.python.org/packages/source/p/pip/pip-1.4.1.tar.gz

tar zxvf pip-1.4.1.tar.gz

cd pip-1.4.1

python setup.py install


下面来看一下pip的使用：

安装包
pip install django

安装特定版本的package，通过使用==, >=, <=, >, <来指定一个版本号。

pip install 'Markdown<2.0'

pip install 'Markdown>2.0,<2.0.3'


升级包到当前最新的版本，可以使用-U 或者 --upgrade

pip install -U Markdown

卸载包

pip uninstall Markdown


查询包

pip search "multiprocessing"


列出安装的packages

$ pip freeze

查看所有安装的包：

pip list
