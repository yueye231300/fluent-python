# 1.1 
from  collections import namedtuple
Card = namedtuple('Card', ['rank', 'suit'])
class FrenchDeck:
    # ranks和suits是类属性
    ranks = [str(n) for n in range(2,11)]+list('JQKA')
    # 使用空格划分字符，传回列表
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        # 只有属性没有方法，self.suits 和self.ranks是实例属性
        self._cards = [Card(rank,suit) for suit in self.suits 
                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
#----- 示例创建，但是没有方法
beer_card  = Card('7','diamonds')
beer_card
#----- 示例创建，使用magic method来得到长度，避免自己写方法忘记
deck = FrenchDeck()
len(deck)
#----- 示例创建，可以调用python标准库，减少自己造轮子的风险。
from random import choice 
choice(deck)

# -----使用__getitem__方法来实现切片
deck[:3]
deck[12::13]
# -----使用__getitem__方法进行迭代
for card in deck:
    print(card)

# -----迭代之后使用in方法，等于扫一遍数据
Card('Q','hearts') in deck

# -----进行纸牌的排序
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck,key=spades_high):
    print(card)

# -----一个简单二维向量类
import math 
class Vector:
    # 构建特殊方法之后不需要直接调用这些函数，而是使用python自带的表达方式
    def __init__(self,x=0,y=0):
        self.x =x 
        self.y =y
    
    def __repr__(self):
        # !r用于__repr__方法的调试
        return f'Vector({self.x!r}, {self.y!r})'
    
    def __abs__(self):
        return math.hypot(self.x,self.y)
    
    def __bool__(self):
        # 除非向量的长度为0，否则返回True
        return bool(abs(self))
    
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    def __mul__(self,scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
v1 = Vector(2,4)
v2 = Vector(2,1)
# +法对应的是__add__方法
v1 + v2
# *法对应的是__mul__方法
v1*5
v2
v0 = Vector()
# -----使用__bool__方法来判断向量是否为0
if v0:
    print('v0 is True')
else:
    print('v0 is False')

