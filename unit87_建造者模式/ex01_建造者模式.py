from abc import ABCMeta, abstractmethod

class Builder(object, metaclass=ABCMeta):
    def __init__(self):
        self.build_part_a()
        self.build_part_b()
    @abstractmethod
    def build_part_a(self): raise NotImplementedError
    @abstractmethod
    def build_part_b(self): raise NotImplementedError

class BuilderA(Builder):
    def build_part_a(self): return 'builderA parta'
    def build_part_b(self): return 'builderA partb'

class BuilderB(Builder):
    def build_part_a(self): return 'builderB parta'
    def build_part_b(self): return 'builderB partb'

class Director(object):
    def __init__(self, builder):
        self.builder = builder
    def build(self):
        return self.builder.build_part_a(), self.builder.build_part_b()

if __name__ == '__main__':
    director = Director(BuilderA())
    print(director.build())
    director.builder = BuilderB()
    print(director.build())
