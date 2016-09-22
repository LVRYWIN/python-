
##coding=utf-8
#正则表达式

# 导入re模块
import re

# 将正则表达式编译成Pattern对象
pattern = re.compile(r'\d+')
print re.split(pattern, 'one1two2three3four4')

### 输出 ###
# ['one', 'two', 'three', 'four', '']


pattern = re.compile(r'hello')

# 使用re.match匹配文本，获得匹配结果，无法匹配时将返回None
result1 = re.match(pattern, 'hello')
result2 = re.match(pattern, 'helloo CQC!')
result3 = re.match(pattern, 'helo CQC!')
result4 = re.match(pattern, 'hello CQC!')

# 如果1匹配成功
if result1:
    # 使用Match获得分组信息
    print result1.group()
else:
    print '1匹配失败！'

# 一个简单的match实例

import re

# 匹配如下内容：单词+空格+单词+任意字符
m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')

print "m.string:", m.string
print "m.re:", m.re
print "m.pos:", m.pos
print "m.endpos:", m.endpos
print "m.lastindex:", m.lastindex
print "m.lastgroup:", m.lastgroup
print "m.group():", m.group()
print "m.group(1,2):", m.group(1, 2)
print "m.groups():", m.groups()
print "m.groupdict():", m.groupdict()
print "m.start(2):", m.start(2)
print "m.end(2):", m.end(2)
print "m.span(2):", m.span(2)
print r"m.expand(r'\g \g\g'):", m.expand(r'\2 \1\3')


#输出全部匹配的
pattern = re.compile(r'\d+')
print re.findall(pattern,'one1two2three3four4')
### 输出 ###
    # [1 2 3 4]

pattern = re.compile(r'\d+')
for m in re.finditer(pattern, 'one1two2three3four4'):
    print m.group(),

    ### 输出 ###
    # 1 2 3 4