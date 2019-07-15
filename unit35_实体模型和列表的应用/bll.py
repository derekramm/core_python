import unit35_实体模型和列表的应用.dal

def choose(flag):
    # 如果没吃饭，可以吃两种水果
    if flag:
        return unit35_实体模型和列表的应用.dal.get_fruit()
    # 如果吃过饭了，只能吃一种水果
    else:
        return unit35_实体模型和列表的应用.dal.get_fruit()[0]
