class A:
    pass


class B:
    n = 5

    def adder(self):
        return self + B.n


a = A()
b = A()
c = B.n
print(c)
print(B.adder(4))


class Purse:
    '''
    __init__ этот код исполняется сразу как создается экземпляр класса
    поля или свойства - переменные в классе
    атрибуты - все имена в классе: переменных и методов
    '''
    def __init__(self, valute, name='Unknown'):
        if valute not in ('USD', 'EUR')
            raise ValueError
        self.__money = 0.00
        self.valute = valute
        self.name = name

    def top_up_balance(self, howmoney):
        self.__money = self.__money + howmoney
        return howmoney

    def top_down_balance(self, howmoney):
        if self.__money - howmoney < 0:
            print('no money')
            raise ValueError ('no money')
        self.__money = self.__money - howmoney
        return howmoney

    def info(self):
        print(self.__money)

    def __del__(self):
        print('del')



x = Purse('USD')
y = Purse('USD', 'Bill')
y.money = 100.00
x.top_up_balance(y.top_down_balance(7))
x.money = -200
x.info()

