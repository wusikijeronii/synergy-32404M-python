class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def print(self):
        print(
            f"Название автомобиля: {self.name} "
            f"Максимальная скорость: {self.max_speed} "
            f"Пробег: {self.mileage}"
        )


class AutobusT(Transport):
    pass

Autobus = AutobusT("Renaul Logan", 180, 12)
Autobus.print()
