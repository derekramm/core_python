from abc import ABCMeta, abstractmethod

class Subject(object):
    def __init__(self):
        self.observers = []
    def attach(self, o): self.observers.append(o)
    def detach(self, o): self.observers.remove(o)
    def notify(self):
        for o in self.observers:
            o.update()

class ConcreteSubject(Subject):
    def __init__(self, state):
        super().__init__()
        self.state = state

class Observer(object, metaclass=ABCMeta):
    @abstractmethod
    def update(self): pass

class ObserverA(Observer):
    def __init__(self, subject):
        self.concrete_subject = subject
        self.concrete_subject.attach(self)
    def update(self): print(f'ObserverA update {self.concrete_subject.state}')

class ObserverB(Observer):
    def __init__(self, subject):
        self.concrete_subject = subject
        self.concrete_subject.attach(self)
    def update(self): print(f'ObserverB update {self.concrete_subject.state}')

if __name__ == '__main__':
    cs = ConcreteSubject('State')
    oa, ob = ObserverA(cs), ObserverB(cs)
    cs.notify()
