class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner
        self._currency = "UAH"  
        if initial_balance < 0: raise ValueError("Баланс не може бути від'ємним")
        self.__balance = initial_balance 

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Сума має бути числом")
        if value < 0:
            raise ValueError("Сума не може бути від'ємною")
        self.__balance = value

    @property
    def info(self):  
        return f"Рахунок {self.owner}: {self.__balance} {self._currency}"

acc = BankAccount("Олексій", 1000)
print(acc.info)

try:
    acc.balance = -500
except ValueError as e:
    print(f"Валідація спрацювала: {e}")

try:
    print(acc.__balance)
except AttributeError:
    print("Прямий доступ до __balance заборонено!")

print(f"Доступ через Name Mangling: {acc._BankAccount__balance}")