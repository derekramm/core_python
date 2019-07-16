from abc import ABCMeta, abstractmethod

class Subject(object, metaclass=ABCMeta):
    @abstractmethod
    def show(self): pass

class RealSubject(Subject):
    def show(self): print(f'RealSubject show()')

class Proxy(Subject):
    def __init__(self): self.real_subject = RealSubject()
    def show(self): self.real_subject.show()

if __name__ == '__main__':
    proxy = Proxy()
    proxy.show()
