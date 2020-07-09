1. 问题
【问题一】 Series和DataFrame有哪些常见属性和方法？
    A:
    Series: index;values;name;dtype;mean()
    DataFrame: index;values;colums;shape;mean()

【问题二】 value_counts会统计缺失值吗？
    A:不会统计缺失数据

【问题三】 如果有多个索引同时取到最大值，idxmax会返回所有这些索引吗？如果不会，那么怎么返回这些索引？
    A:不会，返回最大值第一次出现的位置的索引

【问题四】 在常用函数一节中，由于一些函数的功能比较简单，因此没有列入，现在将它们列在下面，请分别说明它们的用途并尝试使用。
sum/mean/median/mad/min/max/abs/std/var/quantile/cummax/cumsum/cumprod

【问题五】 df.mean(axis=1)是什么意思？它与df.mean()的结果一样吗？问题四提到的函数也有axis参数吗？怎么使用？
【问题六】 对值进行排序后，相同的值次序由什么决定？¶
【问题七】 Pandas中为各类基础运算也定义了函数，比如s1.add(s2)表示两个Series相加，但既然已经有了'+'，是不是多此一举？
【问题八】 如果DataFrame某一列的元素是numpy数组，那么将其保存到csv在读取后就会变成字符串，怎么解决？
