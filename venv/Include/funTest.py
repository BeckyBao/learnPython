#函数
'''
#练习1
def matrix(a,b,c):
    print('乘积为：',a*b*c)
matrix(10,3,9)

#练习2
def welcom(name):
    print('欢迎',name,'的到来！')
welcom('becky')
'''
#文档字符串

def fn(a,b,v):
    '''
    这是一个文档字符串
    :param a: 作用，类型，默认
    :param b: 作用，类型，默认
    :param v: 作用，类型，默认
    :return:
    '''
    print('weloom')
#help(fn)

'''
#命名空间
a = globals()
print(a)
'''
#递归
#求任意数的阶乘
def factorial(a):
    '''
    该函数用来求任意数的阶乘
    :param a: 要求阶乘的数字
    :return:
    '''
    #创建一个变量保存结果
    result = a
    for i in range(1,a):
        result *= i
    return result

#print( '10的阶乘是：',factorial(10))

#递归式函数，在函数中自己调用自己
def factorial2(a):
    '''
    该函数用来求任意数的阶乘
    :param a: 要求阶乘的数字
    :return:
    '''
    #基线条件判断a是否为1，若为1则不能进行递归
    if a == 1:
        #1的阶乘就是1，直接返回
        return 1
    return a * factorial2(a -1)

#print( '10的阶乘是：',factorial2(10))

#递归练习
#1.任意数字的幂运算
def power(n,i):
    '''
    计算传入参数的幂运算
    :param n: 要做幂运算的数字
    :param i: 做幂运算的次数
    :return:
    '''
    #基线条件
    if i == 1:
        #求1次幂
        return n
    #递归条件
    return n *power(n,i-1)
print('8的6次幂是：',power(8,6))

#2.回文字符串检测
def hw_check(s):
    '''
    该函数用于检测传入字符串是否为回文字符串，是返回true，不是返回false
    :param s:用于检测的字符串
    :return:
    '''
    #基线条件
    if len(s)<2:
        #字符串长度小于2，则字符串一定是回文
        return True
    elif s[0] != s[-1]:
        #第一个字符和最后一个不相等，不是回文字符串
        return False
    #递归条件
    return hw_check(s[1:-1])
#print(hw_check('aabbbbaa'))

#高级函数
#将指定列表中的所有偶数，保存到一个新列表并返回
def fn(lst):
    #定义一个函数，用来检测一个数字的奇偶
    def fn2(n):
        if n % 2 == 0:
            return True
        return False
    '''
    fn（）可以将指定列表中的所有偶数，保存到一个新列表并返回
    :param list:
    :return:
    '''
    #常见一个新列表
    new_list = []
    #队列表进行筛选
    for n in lst:
        #判断n的奇偶
        if fn2(n):
            new_list.append(n)
    return new_list
print(fn([2,3,2,3,44,55,3]))

#匿名函数
#filter()可以从序列中过滤出符合条件的元素，保存到新的序列
#map()可以对所有元素进行指定操作，将其添加到一个新的对象中返回
#sort()方法默认比较列表元素的大小
l = [2,3,1,44,3,2,3]
r = filter(lambda i : i > 5,l)
r2 = filter(lambda i : i **2,l)
r3 = map(lambda i : i + 1,l)
l.sort(key=int)
print(list(r),'\n',list(r2),'\n',list(r3),'\n',l)
#闭包
def make_average():
    nums = []
    def average(n):
        nums.append(n)
        return sum(nums)/len(nums)
    return average
aaa = make_average()
print(aaa(10))
print(aaa(22))

