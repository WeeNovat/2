from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message): pass
    
    @property
    @abstractmethod
    def status(self): pass

class ConsoleLogger(Logger):
    def log(self, message): print(f"[LOG]: {message}")
    @property
    def status(self): return "Active"

class Order:
    def __init__(self, item, price, logger: Logger):
        self.item = item
        self.price = price
        self.logger = logger

    def process(self):
        self.logger.log(f"Обробка замовлення {self.item} на суму {self.price}")

try:
    Logger()
except TypeError:
    print("Неможливо створити екземпляр абстрактного класу!")

order = Order("Laptop", 25000, ConsoleLogger())
order.process()
