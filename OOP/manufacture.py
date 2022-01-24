class Machine:

    def __init__(self, productivity_k=0.8, day=0, exe_4=False):
        # Производительность оборудования 0,8 по умолчанию
        self.productivity_k = productivity_k
        # Время работы  в размерности timestamp
        self.time_work = day * 16 * 60 * 60
        self.productivity = int(self.time_work * self.productivity_k)
        self.exe_4 = exe_4


a = Machine(day=7)
print(a.__dict__)
