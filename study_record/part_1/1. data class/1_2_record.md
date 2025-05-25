# 丰富的序列

## 2.2 内置序列

内置序列

- 按照存储数据的类型：
  - 容器序列，可以用来存储不同类型数据
  - 扁平序列，只能存储同一类型数据

- 按照存储数据的方式：
  - 可变序列，可以修改数据
  - 不可变序列，不能修改数据，例如tuple,str,bytes等

## 2.3 列表生成式

使用列表生成式快速构建列表并可以使用笛卡尔积来得到多个迭代元组
示例

```python
colors = ['red','green']
sizes = ['S','M','L']
suits = ['a','b']
tshirts = [(color,size,suit) for color in colors 
                        for size in sizes
                        for suit in suits]
tshirts
```

## 生成器表达式

生成器占用内存更少，逐个迭代出现结果

示例：

```python
color = ['white','green']
size =['S','M','L']
for tshirt in (f'{c}{s}' for c in color for s in size):
    print(tshirt)
```

## 2.4 元组

元组可以用来记录，并不是不可变的列表，记录信息与位置有关，元组的元素与所在的位置有关，所以不能随意排列位置。

元组作为不可变列表的作用，长度固定以及性能优化。但是不可变值的是引用对象，元组中使用可变序列可能会出现问题，见例子：

```python
a = (10,'alpha',[1,2])
b = (10,'alpha',[1,2])
print(a==b)
b[-1].append(9999)
print(a==b)
b
```

判断值是否固定可以采用hash函数,例子如下：

```python
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
```

## 序列与可迭代对象的拆包

直接通过*可完成所有元素的传递。在函数传递的参数中使用

```python
a,b,*rest = range(5)
print(rest)
```
