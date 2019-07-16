#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex07_文件对象操作_write.py"""

# 将字符串或bytes类型的数据写入文件内
# write()动作可以多次重复进行，其实都是在内存中的操作，并不会立刻写回硬盘
# 直到执行close()方法后，才会将所有的写入操作反映到硬盘上
# 在这过程中，如果想将内存中的修改，立刻保存到硬盘上，可以使用f.flush()方法
# 但这可能造成数据的不一致

# 打开一个文件
f = open("about.txt", "w")
f.write("Hello\nPython World!\n")

# 关闭打开的文件
f.close()