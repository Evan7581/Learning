# -*- coding: utf-8 -*-

# 制作9x9乘法表
mother = '{item1}x{item2}={item3}'
li_table = []
for x in range(1, 10):
    li_line = []
    for y in range(1, 10):
        if x >= y:
            li_line.append(mother.format(item1=y, item2=x, item3=x * y))
    li_table.append(li_line)
for i in li_table:
    print(' '.join(i))
