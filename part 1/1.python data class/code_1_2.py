# 列表推导式
symbols = 'abcded'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

X = 'ABC'
codes = [ord(x) for x in X]
codes
codes = [last:=ord(x) for x in X]
last

# 笛卡尔积
colors = ['red','green']
sizes = ['S','M','L']
suits = ['a','b']
tshirts = [(color,size,suit) for color in colors 
                        for size in sizes
                        for suit in suits]
tshirts

# 生成器
symbols = 'abcded'
codes = tuple(ord(symbol) for symbol in symbols)
codes 

# 不是一起产生的列表推导式,而是逐个产生的生成器迭代器
color = ['white','green']
size =['S','M','L']
for tshirt in (f'{c}{s}' for c in color for s in size):
    print(tshirt)

# 元组
lax_coordinates = (33.9425, -118.408056)
# 可以直接使用元组吗？
city,year,pop,chg,area = ('Tokyo', 2003, 9.273, 0.66, 8014)
traveler_ids = [('USA','31195855'),('BRA','CE342567'),('ESP','XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)
for country,_ in traveler_ids:
    print(country)
    print(_)

# 元组引用变化
a = (10,'alpha',[1,2])
b = (10,'alpha',[1,2])
print(a==b)
b[-1].append(9999)
print(a==b)
b

# 元素是否可变
def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True

tf = (10,'alpha',[1,2])
tm =(10,'alpha',(1,2))
print(fixed(tf))
print(fixed(tm))

# 拆包
a,b,*rest = range(5)
print(rest)