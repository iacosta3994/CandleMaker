class candleContainerClass:
    def __init__(self,maxVolume,quantity, price):
        self.maxVolume = maxVolume
        self.quantity = quantity
        self.price = price
    
    def fillContainers (self,totalWeight):
        self.weightPerContainer = totalWeight / self.quantity
        self.MaxVolumeInGrams = self.maxVolume * 29.5735296875
        self.filledContainers = 