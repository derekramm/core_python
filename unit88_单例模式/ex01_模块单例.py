from unit88_单例模式.singleton_module import singleton


if __name__ == '__main__':

    s1, s2 = singleton, singleton
    print(id(s1), id(s2))
