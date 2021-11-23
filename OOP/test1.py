class A:
    pass


class B:
    n = 5

    def adder(v):
        return v + B.n


a = A()
b = A()
c = B.n
print(c)
print(B.adder(4))