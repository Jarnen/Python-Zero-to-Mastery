class A:
    def process(self):
        print('A process()')


class B:
    def process(self):
        print('B process()')


class C(A, B):
    print('C process')


class D(C, B):
    pass


obj = D()
obj.process()
print(D.mro())
