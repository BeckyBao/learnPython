#类
#定义一个简单的类，用class关键字来定义
#自定义类都要使用大写字母开头，用大驼峰命名法对类命名
#class 类名([父类])
class MyClass():
    pass
#print(MyClass)
#使用MyClass创建一个对象
mc = MyClass() #mc就是MyClass的实例
#isinstance（）用来检查一个对象是不是一个类的实例
result = isinstance(mc,MyClass)
#print(result)

class Person:
    #在类代码块里，可以定义函数和变量
    #在类中定义的变量，会成为所有实例的公共属性
    name = 'swk'#公共属性，所有实例都可以访问
    #类中定义函数，称之为方法，可以通过该类的所有实例来访问
    #创建对象的流程
    #p1 = Person()的运行流程
    # 1.创建一个变量
    # 2.在内存中创建一个新对象
    # 3.__init__(self)方法执行
    # 4.将对象的id赋值给变量

    #init会在对象创建以后立刻开始执行
    #init可以用来相信的对象初始化属性
    def __int__(self,name):
        self.name = name
    #调用类的创建对象时，类后面的所有参数都会依次传递到init（）中
    def say_hello(self):
        #方法被调用是解析器会自动传递第一个实参
        #第一个参数，就是调用方法的对象本身，可以用self定义传入参数
        print('hello!我是%s'%self.name)

p1 = Person()
p2 = Person()
p1.name = 'aaa'
p1.say_hello()
p2.say_hello()

#封装
#是面向对象的三大特性之一
#封装指的是隐藏对象中一些不希望被外部所访问到的属性和方法

class Dog:
    '''
    表是狗的类
    '''
    def __init__(self,name):
        self.hidden_name = name
    def say_hello(self):
        print('大家好，我是%s'%self.hidden_name)
    def get_name(self):
        '''
        get_name()用来获取对象的name属性
        '''
        return  self.hidden_name
    def set_name(self,name):
        self.hidden_name = name
d = Dog('lucky')
d.say_hello()

d.set_name('cindy')
d.say_hello()

class Cat:
    def __init__(self,name):
        self._name = name
        # property装饰器，用来讲一个get方法转换为对象的属性
        # 添加为property装饰器以后，我们就可以像调用属性一样使用get方法
        # 使用property装饰的方法，必须和属性名一样的
        @property
        def name(self):
            print('get方法执行了~')
            return self._name
        #setter方法的装饰器，@属性名.setter
        @name.setter
        def name(self,name):
            print('set方法执行了~')
            self._name = name
c = Cat('咪咪')
c.name = '乖乖'
print(c.name)

#继承
class Animal:
    def run(self):
        print('动物会跑~')
    def sleep(self):
        print('动物睡觉~')
#在定义类时，可以在类名后的括号指定当前类的父类
class Bird(Animal):
    def fly(self):
        print('小鸟会飞~')

b = Bird()
b.sleep()
b.fly()
