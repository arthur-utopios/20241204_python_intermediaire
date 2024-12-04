class WaterTank:

    volume_total = 0

    def __init__(self, weight: float, volume_max: float, volume: float) -> None:
        self.weight = weight
        self.volume_max = volume_max
        self.volume = volume
        WaterTank.volume_total += volume

    def fill(self, volume: float) -> None:
        if self.volume + volume > self.volume_max:
            WaterTank.volume_total += self.volume_max - self.volume
            self.volume = self.volume_max
        else:
            self.volume += volume
            WaterTank.volume_total += volume

    def drain(self, volume: float) -> None:
        if self.volume - volume < 0:
            WaterTank.volume_total -= self.volume
            self.volume = 0
        else:
            self.volume -= volume
            WaterTank.volume_total -= volume

    @property
    def total_weigth(self):
        return self.weight + self.volume
    
    def __str__(self) -> str:
        return f"Watertank = poids: {self.weight}kg, volume: {self.volume}/{self.volume_max}L, poids total: {self.total_weigth}kg"
    
if __name__ == "__main__":
    watertank1 = WaterTank(12, 100, 5)
    print(watertank1)
    print(watertank1.total_weigth)

    watertank1.fill(10)
    print(watertank1)

    watertank1.fill(100)
    print(watertank1)

    watertank1.drain(150)
    print(watertank1)

    print(WaterTank.volume_total)

    watertank2 = WaterTank(20, 50, 2)
    watertank1.fill(50)
    watertank2.fill(4)

    print(watertank1)
    print(watertank2)
    print(WaterTank.volume_total, "L")