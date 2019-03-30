---
layout: post
title: Python包管理工具setuptools详解
category: 技术
tags: Python
keywords: Python Setuptools
description: setuptools可能在未来被distutils2代替，但是现在用到的还挺多，需要学习一下，有利于读Python代码。
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

### 0.什么是setuptools
setuptools是Python distutils增强版的集合，它可以帮助我们更简单的创建和分发Python包，尤其是拥有依赖关系的。用户在使用setuptools创建的包时，并不需要已安装setuptools，只要一个[启动模块](http://peak.telecommunity.com/dist/ez_setup.py)即可。

功能亮点：

- 利用[EasyInstall](http://peak.telecommunity.com/DevCenter/EasyInstall)自动查找、下载、安装、升级依赖包
- 创建[Python Eggs](http://peak.telecommunity.com/DevCenter/PythonEggs)
- 包含包目录内的数据文件
- 自动包含包目录内的所有的包，而不用在setup.py中列举
- 自动包含包内和发布有关的所有相关文件，而不用创建一个MANIFEST.in文件
- 自动生成经过包装的脚本或Windows执行文件
- 支持Pyrex，即在可以setup.py中列出.pyx文件，而最终用户无须安装Pyrex
- 支持上传到PyPI
- 可以部署开发模式，使项目在sys.path中
- 用新命令或setup()参数扩展distutils，为多个项目发布/重用扩展
- 在项目setup()中简单声明entry points，创建可以自动发现扩展的应用和框架

总之，setuptools就是比distutils好用的多，基本满足大型项目的安装和发布

### 1.安装setuptools
1) 最简单安装，假定在ubuntu下

    sudo apt-get install python-setuptools

2) 启动脚本安装

    wget http://peak.telecommunity.com/dist/ez_setup.py
    sudo python ez_setup.py

### 2.创建一个简单的包
有了setuptools后，创建一个包基本上是无脑操作

    cd /tmp 
    mkdir demo
    cd demo

在demo中创建一个`setup.py`文件，写入

    from setuptools import setup, find_packages
    setup(
        name = "demo",
        version = "0.1",
        packages = find_packages(),
    )

执行`python setup.py bdist_egg`即可打包一个test的包了。

    demo
    |-- build
    |   `-- bdist.linux-x86_64
    |-- demo.egg-info
    |   |-- dependency_links.txt
    |   |-- PKG-INFO
    |   |-- SOURCES.txt
    |   `-- top_level.txt
    |-- dist
    |   `-- demo-0.1-py2.7.egg
    `-- setup.py

在dist中生成的是egg包

    file dist/demo-0.1-py2.7.egg
    dist/demo-0.1-py2.7.egg: Zip archive data, at least v2.0 to extract

看一下生成的.egg文件，是个zip包，解开看看先

    upzip -l dist/demo-0.1-py2.7.egg

    Archive:  dist/demo-0.1-py2.7.egg
      Length      Date    Time    Name
    ---------  ---------- -----   ----
            1  2013-06-07 22:03   EGG-INFO/dependency_links.txt
            1  2013-06-07 22:03   EGG-INFO/zip-safe
          120  2013-06-07 22:03   EGG-INFO/SOURCES.txt
            1  2013-06-07 22:03   EGG-INFO/top_level.txt
          176  2013-06-07 22:03   EGG-INFO/PKG-INFO
    ---------                     -------
          299                     5 files

我们可以看到，里面是一系列自动生成的文件。现在可以介绍一下刚刚setup()中的参数了

- name 包名
- version 版本号
- packages 所包含的其他包

要想发布到PyPI中，需要增加别的参数，这个可以参考[官方文档](http://pythonhosted.org/setuptools/setuptools.html#basic-use)中的例子了。

### 3.给包增加内容
上面生成的egg中没有实质的内容，显然谁也用不了，现在我们稍微调色一下，增加一点内容。

在demo中执行`mkdir demo`，再创建一个目录，在这个demo目录中创建一个`__init__.py`的文件，表示这个目录是一个包，然后写入：

    #!/usr/bin/env python
    #-*- coding:utf-8 -*-

    def test():
        print "hello world!"  

    if __name__ == '__main__':
        test()

现在的主目录结构为下：

    demo
    |-- demo
    |   `-- __init__.py
    `-- setup.py

再次执行`python setup.py bdist_egg`后，再看egg包

    Archive:  dist/demo-0.1-py2.7.egg
      Length      Date    Time    Name
    ---------  ---------- -----   ----
            1  2013-06-07 22:23   EGG-INFO/dependency_links.txt
            1  2013-06-07 22:23   EGG-INFO/zip-safe
          137  2013-06-07 22:23   EGG-INFO/SOURCES.txt
            5  2013-06-07 22:23   EGG-INFO/top_level.txt
          176  2013-06-07 22:23   EGG-INFO/PKG-INFO
           95  2013-06-07 22:21   demo/__init__.py
          338  2013-06-07 22:23   demo/__init__.pyc
    ---------                     -------
          753                     7 files

这回包内多了demo目录，显然已经有了我们自己的东西了，安装体验一下。

    python setup.py install

这个命令会讲我们创建的egg安装到python的dist-packages目录下，我这里的位置在

    tree /usr/local/lib/python2.7/dist-packages/demo-0.1-py2.7.egg

查看一下它的结构：

    /usr/local/lib/python2.7/dist-packages/demo-0.1-py2.7.egg
    |-- demo
    |   |-- __init__.py
    |   `-- __init__.pyc
    `-- EGG-INFO
        |-- dependency_links.txt
        |-- PKG-INFO
        |-- SOURCES.txt
        |-- top_level.txt
        `-- zip-safe

打开python终端或者ipython都行，直接导入我们的包
    
    >>> import demo
    >>> demo.test()
    hello world!
    >>>

好了，执行成功！

### 4.setuptools进阶
在上例中，在前两例中，我们基本都使用setup()的默认参数，这只能写一些简单的egg。一旦我们的project逐渐变大以后，维护起来就有点复杂了，下面是setup()的其他参数，我们可以学习一下

#### 使用find_packages()
对于简单工程来说，手动增加packages参数很容易，刚刚我们用到了这个函数，它默认在和setup.py同一目录下搜索各个含有`__init__.py`的包。其实我们可以将包统一放在一个src目录中，另外，这个包内可能还有aaa.txt文件和data数据文件夹。

    demo
    ├── setup.py
    └── src
        └── demo
            ├── __init__.py
            ├── aaa.txt
            └── data
                ├── abc.dat
                └── abcd.dat
            
如果不加控制，则setuptools只会将`__init__.py`加入到egg中，想要将这些文件都添加，需要修改`setup.py`

    from setuptools import setup, find_packages
    setup(
        packages = find_packages('src'),  # 包含所有src中的包
        package_dir = {'':'src'},   # 告诉distutils包都在src下

        package_data = {
            # 任何包中含有.txt文件，都包含它
            '': ['*.txt'],
            # 包含demo包data文件夹中的 *.dat文件
            'demo': ['data/*.dat'],
        }
    )

这样，在生成的egg中就包含了所需文件了。看看：

    Archive:  dist/demo-0.0.1-py2.7.egg
      Length     Date   Time    Name
     --------    ----   ----    ----
           88  06-07-13 23:40   demo/__init__.py
          347  06-07-13 23:52   demo/__init__.pyc
            0  06-07-13 23:45   demo/aaa.txt
            0  06-07-13 23:46   demo/data/abc.dat
            0  06-07-13 23:46   demo/data/abcd.dat
            1  06-07-13 23:52   EGG-INFO/dependency_links.txt
          178  06-07-13 23:52   EGG-INFO/PKG-INFO
          157  06-07-13 23:52   EGG-INFO/SOURCES.txt
            5  06-07-13 23:52   EGG-INFO/top_level.txt
            1  06-07-13 23:52   EGG-INFO/zip-safe
     --------                   -------
          777                   10 files

另外，也可以排除一些特定的包，如果在src中再增加一个tests包，可以通过exclude来排除它,

    find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])

#### 使用entry_points
一个字典，从entry point组名映射道一个表示entry point的字符串或字符串列表。Entry points是用来支持动态发现服务和插件的，也用来支持自动生成脚本。这个还是看例子比较好理解：

    setup(
        entry_points = {
            'console_scripts': [
                'foo = demo:test',
                'bar = demo:test',
            ],
            'gui_scripts': [
                'baz = demo:test',
            ]
        }
    )

修改`setup.py`增加以上内容以后，再次安装这个egg，可以发现在安装信息里头多了两行代码（Linux下）：

    Installing foo script to /usr/local/bin
    Installing bar script to /usr/local/bin

查看`/usr/local/bin/foo`内容

    #!/usr/bin/python
    # EASY-INSTALL-ENTRY-SCRIPT: 'demo==0.1','console_scripts','foo'
    __requires__ = 'demo==0.1'
    import sys
    from pkg_resources import load_entry_point

    if __name__ == '__main__':
        sys.exit(
            load_entry_point('demo==0.1', 'console_scripts', 'foo')()
        )

这个内容其实显示的意思是，foo将执行console_scripts中定义的foo所代表的函数。执行foo，发现打出了`hello world!`，和预期结果一样。

#### 使用Eggsecutable Scripts
从字面上来理解这个词，Eggsecutable是Eggs和executable合成词，翻译过来就是另eggs可执行。也就是说定义好一个参数以后，可以另你生成的.egg文件可以被直接执行，貌似Java的.jar也有这机制？不很清楚，下面是使用方法：

    setup(
        # other arguments here...
        entry_points = {
            'setuptools.installation': [
                'eggsecutable = demo:test',
            ]
        }
    )

这么写意味着在执行`python *.egg`时，会执行我的test()函数，在文档中说需要将.egg放到PATH路径中。

#### 包含数据文件
在3中我们已经列举了如何包含数据文件，其实setuptools提供的不只这么一种方法，下面是另外两种

1）包含所有包内文件

这种方法中包内所有文件指的是受版本控制（CVS/SVN/GIT等）的文件，或者通过MANIFEST.in声明的

    from setuptools import setup, find_packages
    setup(
        ...
        include_package_data = True
    )

2）包含一部分，排除一部分

    from setuptools import setup, find_packages
    setup(
        ...
        packages = find_packages('src'),  
        package_dir = {'':'src'},   

        include_package_data = True,    

        # 排除所有 README.txt
        exclude_package_data = { '': ['README.txt'] },
    )

如果没有使用版本控制的话，可以还是使用3中提到的包含方法

#### 可扩展的框架和应用
setuptools可以帮助你将应用变成插件模式，供别的应用使用。官网举例是一个帮助博客更改输出类型的插件，一个博客可能想要输出不同类型的文章，但是总自己写输出格式化代码太繁琐，可以借助一个已经写好的应用，在编写博客程序的时候动态调用其中的代码。

通过entry_points可以定义一系列接口，供别的应用或者自己调用，例如：

    setup(
        entry_points = {'blogtool.parsers': '.rst = some_module:SomeClass'}
    )

    setup(
        entry_points = {'blogtool.parsers': ['.rst = some_module:a_func']}
    )

    setup(
        entry_points = """
            [blogtool.parsers]
            .rst = some.nested.module:SomeClass.some_classmethod [reST]
        """,
        extras_require = dict(reST = "Docutils>=0.3.5")
    )

上面列举了三中定义方式，即我们将我们some_module中的函数，以名字为blogtool.parsers的借口共享给别的应用。

别的应用使用的方法是通过`pkg_resources.require()`来导入这些模块。

另外，一个名叫[stevedore](http://stevedore.readthedocs.org/en/latest/index.html)的库将这个方式做了封装，更加方便进行应用的扩展。

### 5. 以后增加
以上内容大部分来自于[官方文档](http://pythonhosted.org/setuptools/setuptools.html)，需要额外学习的以后再增加





