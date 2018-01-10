# coding=utf-8

# -*- coding: utf-8 -*-


class Person:
    def __init__(self, name):
        self.name = name


class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email


if __name__ == '__main__':
    baoyu = EmailPerson('宝玉', 'baoyu@ivix.me')

    print('「姓名」', baoyu.name, '「邮箱」', baoyu.email)


# 使用属性对特性进行访问和设置
#
# @property 用于指示getter方法
# @PROPERTY_NAME.setter 用于指示setter方法

class Circle:
    """圆形"""

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius


if __name__ == '__main__':
    c = Circle(5)
    print('半径：%d，直径：%d' % (c.radius, c.diameter))

class Duck:
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print('getter')
        return self.hidden_name

    def set_name(self, input_name):
        print('setter')
        self.hidden_name = input_name

    name = property(get_name, set_name)


donald = Duck('唐老鸭')
print(donald.name)
donald.name = 'Donald Duck'
print(donald.name)

class Duck1:
    def __init__(self, input_name, gender):
        self.hidden_name = input_name
        self.hidden_gender = gender

    @property
    def name(self):
        print('name getter')
        return self.hidden_name

    @name.setter
    def name(self, input_name):
        print('name setter')
        self.hidden_name = input_name

    @property
    def gender(self):
        return self.hidden_gender

    @gender.setter
    def gender(self, gender):
        self.hidden_gender = gender



donald = Duck1('唐老鸭', '公')
print(donald.name, '是只欢乐的小', donald.gender, '鸭')

# 方法的类型
#
# 以self作为第1个参数的方法都是实例方法
#
# 用装饰器@classmetchod修饰的方法都是类方法，
# 第一个参数是类本身，这个参数常被写作cls
#
# 使用@staticmethod修饰的方法是静态方法，既不会影响类也不会影响类的对象。
# 它们的出现仅仅是为了方便，否则它们只能孤零零地出现在代码的其它地方，影响代码的逻辑，
# 既不用self参数，也不用cls参数

class A:
    count = 0  # 类特性

    def __init__(self):
        A.count += 1

    def exclaim(self):
        print("I'm an A!")

    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.") # cls.count与A.count的作用一样


if __name__ == '__main__':
    a1 = A()
    a2 = A()
    a3 = A()
    A.kids()


class CoyoteWeapon:
    @staticmethod #静态方法
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')


CoyoteWeapon.commercial()

# 多态(鸭子类型, duck typing)


class Quote:
    def __init__(self, person, words):
        self.person = person
        self.words = words

    def who(self):
        return self.person

    def says(self):
        return self.words + '.'


class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'


class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'


class BabblingBrook:
    def who(self):
        return 'Brook'

    def says(self):
        return 'Babble'


def who_says(obj):
    print(obj.who(), 'says', obj.says())


hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc")
hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
brook = BabblingBrook()

who_says(hunter)
who_says(hunted1)
who_says(hunted2)
who_says(brook)

# 特殊方法(魔术方法)
#
# |方法名|使用|
# |----|----|
# |`__eq__(self, other)`|`self == other`|
# |`__ne__(self, other)`|`self != other`|
# |`__lt__(self, other)`|`self < other`|
# |`__gt__(self, other)`|`self > other`|
# |`__le__(self, other)`|`self <= other`|
# |`__ge__(self, other)`|`self >= other`|
# |`__add__(self, other)`|`self + other`|
# |`__sub__(self, other)`|`self - other`|
# |`__mul__(self, other)`|`self * other`|
# |`__floordiv__(self, other)`|`self // other`|
# |`__truediv__(self, other)`|`self / other`|
# |`__mod__(self, other)`|`self % other`|
# |`__pow__(self, other)`|`self ** other`|
# |`__str__(self)`|`str(self)`|
# |`__repr__(self)`|`repr(self)`|
# |`__len__(self)`|`len(self)`|

class Word:
    def __init__(self, text):
        self.text = text

    def __eq__(self, w):
        return self.text.lower() == w.text.lower()

    def __str__(self):
        return self.text

    def __repr__(self):
        return 'Word("' + self.text + '")'

    def __add__(self, other):
        return self.text + other.text

    def __mul__(self, other):
        try:
            num = int(other)
            return self.text * num
        except:
            return self.text


first = Word('ha')
second = Word('HA')
third = Word('eh')
four = Word("8")

print(first, second, third)
print(first + third)
print(first * 8)
print(four * 8)


class Bill:
    def __init__(self, description):
        self.description = description


class Tail:
    def __init__(self, length):
        self.length = length


class Duck:
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail

    def about(self):
        print('This duck has a', self.bill.description, 'bill and a', self.tail.length, 'tail')


tail = Tail('long')
bill = Bill('wide orange')
duck = Duck(bill, tail)
duck.about()