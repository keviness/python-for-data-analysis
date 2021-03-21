# NumPy与输入输出
## 使用genfromtxt导入数据
NumPy提供了几个函数来根据表格数据创建数组。我们将重点放在genfromtxt函数上。

In a nutshell, genfromtxt runs two main loops. 第一个循环以字符串序列转换文件的每一行。第二个循环将每个字符串转换为适当的数据类型。这种机制比单一循环慢，但提供了更多的灵活性。特别的, genfromtxt考虑到缺失值的情况, 其他更简单的方法如loadtxt无法做到这点.

注意 举例时，我们将使用以下约定：
~~~py
>>> import numpy as np
>>> from io import BytesIO
~~~
### 定义输入
> genfromtxt的唯一强制参数是数据的来源。它可以是一个字符串，一串字符串或一个生成器。如果提供了单个字符串，则假定它是本地或远程文件的名称，或者带有read方法的开放文件类对象，例如文件或StringIO.StringIO对象。如果提供了字符串列表或生成器返回字符串，则每个字符串在文件中被视为一行。当传递远程文件的URL时，该文件将自动下载到当前目录并打开。

识别的文件类型是文本文件和档案。目前，该功能可识别gzip和bz2（bzip2）档案。归档文件的类型由文件的扩展名决定：如果文件名以'.gz'结尾，则需要一个gzip归档文件；如果它以'bz2'结尾，则假定bzip2存档。

### 将行拆分为列
#### delimiter参数
一旦文件被定义并打开进行读取，genfromtxt会将每个非空行分割为一串字符串。 空的或注释的行只是略过。 delimiter关键字用于定义拆分应该如何进行。

通常，单个字符标记列之间的分隔。例如，逗号分隔文件（CSV）使用逗号（,）或分号（;）作为分隔符：
~~~py
>>> data = "1, 2, 3\n4, 5, 6"
>>> np.genfromtxt(BytesIO(data), delimiter=",")
array([[ 1.,  2.,  3.],
       [ 4.,  5.,  6.]])
~~~
另一个常用的分隔符是"\t"，即制表符。但是，我们不限于单个字符，任何字符串都可以。默认情况下，genfromtxt假定delimiter=None，这意味着该行沿着空白区域（包括制表符）分割，并且连续的空白区域被视为单个空白区域。

或者，我们可能正在处理一个固定宽度的文件，其中列被定义为给定数量的字符。在这种情况下，我们需要将delimiter设置为单个整数（如果所有列的大小相同）或整数序列（如果列的大小可能不同）：
~~~py
>>> data = "  1  2  3\n  4  5 67\n890123  4"
>>> np.genfromtxt(BytesIO(data), delimiter=3)
array([[   1.,    2.,    3.],
       [   4.,    5.,   67.],
       [ 890.,  123.,    4.]])
>>> data = "123456789\n   4  7 9\n   4567 9"
>>> np.genfromtxt(BytesIO(data), delimiter=(4, 3, 2))
array([[ 1234.,   567.,    89.],
       [    4.,     7.,     9.],
       [    4.,   567.,     9.]])
~~~

### autostrip参数
> 默认情况下，当一行被分解为一系列字符串时，单个条目不会被剥离前导空白或尾随空白。通过将可选参数autostrip设置为值True，可以覆盖此行为：
~~~py
>>> data = "1, abc , 2\n 3, xxx, 4"
>>> # Without autostrip
>>> np.genfromtxt(BytesIO(data), delimiter=",", dtype="|S5")
array([['1', ' abc ', ' 2'],
       ['3', ' xxx', ' 4']],
      dtype='|S5')
>>> # With autostrip
>>> np.genfromtxt(BytesIO(data), delimiter=",", dtype="|S5", autostrip=True)
array([['1', 'abc', '2'],
       ['3', 'xxx', '4']],
      dtype='|S5')
~~~
### comments参数
> 可选参数comments用于定义标记注释开始的字符串。默认情况下，genfromtxt假定comments='#'。评论标记可能发生在线上的任何地方。评论标记之后的任何字符都会被忽略：

~~~py
>>> data = """#
... # Skip me !
... # Skip me too !
... 1, 2
... 3, 4
... 5, 6 #This is the third line of the data
... 7, 8
... # And here comes the last line
... 9, 0
... """
>>> np.genfromtxt(BytesIO(data), comments="#", delimiter=",")
[[ 1.  2.]
 [ 3.  4.]
 [ 5.  6.]
 [ 7.  8.]
 [ 9.  0.]]
~~~
这种行为有一个明显的例外：如果可选参数names=True，则会检查第一条注释行的名称。

#### 跳过直线并选择列
##### skip_header和skip_footer参数
> 文件中存在标题可能会妨碍数据处理。在这种情况下，我们需要使用skip_header可选参数。此参数的值必须是一个整数，与执行任何其他操作之前在文件开头跳过的行数相对应。同样，我们可以使用skip_footer属性跳过文件的最后一行n，并给它一个n的值：

~~~py
>>> data = "\n".join(str(i) for i in range(10))
>>> np.genfromtxt(BytesIO(data),)
array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.])
>>> np.genfromtxt(BytesIO(data),
...               skip_header=3, skip_footer=5)
array([ 3.,  4.])
~~~

默认情况下，skip_header=0和skip_footer=0，这意味着不会跳过任何行。

### usecols参数
> 在某些情况下，我们对数据的所有列不感兴趣，但只有其中的一小部分。我们可以用usecols参数选择要导入的列。该参数接受与要导入的列的索引相对应的单个整数或整数序列。请记住，按照惯例，第一列的索引为0。负整数的行为与常规Python负向索引相同。

例如，如果我们只想导入第一列和最后一列，我们可以使用usecols =（0， -1）：
~~~py
>>> data = "1 2 3\n4 5 6"
>>> np.genfromtxt(BytesIO(data), usecols=(0, -1))
array([[ 1.,  3.],
       [ 4.,  6.]])
~~~
如果列有名称，我们也可以通过将它们的名称提供给usecols参数来选择要导入哪些列，可以将其作为字符串序列或逗号分隔字符串：
~~~py
>>> data = "1 2 3\n4 5 6"
>>> np.genfromtxt(BytesIO(data),
...               names="a, b, c", usecols=("a", "c"))
array([(1.0, 3.0), (4.0, 6.0)],
      dtype=[('a', '<f8'), ('c', '<f8')])
>>> np.genfromtxt(BytesIO(data),
...               names="a, b, c", usecols=("a, c"))
    array([(1.0, 3.0), (4.0, 6.0)],
          dtype=[('a', '<f8'), ('c', '<f8')])
~~~

