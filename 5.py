class DeliveryStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, weight): pass

class GroundDelivery(DeliveryStrategy):
    def calculate_cost(self, weight): return weight * 5

class AirDelivery(DeliveryStrategy):
    def calculate_cost(self, weight): return weight * 50

class Courier:
    def __init__(self, strategy: DeliveryStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: DeliveryStrategy):
        self.strategy = strategy

    def deliver(self, weight):
        cost = self.strategy.calculate_cost(weight)
        print(f"Вартість доставки вагою {weight}кг: {cost} грн")


delivery = Courier(GroundDelivery())
delivery.deliver(10)


class DroneDelivery(DeliveryStrategy):
    def calculate_cost(self, weight): return weight * 100

delivery.set_strategy(DroneDelivery())
delivery.deliver(10)
