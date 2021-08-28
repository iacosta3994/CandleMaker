class candleContainerClass:
    def __init__(self,maxVolume,quantity, price):
        self.maxVolume = maxVolume
        self.quantity = quantity
        self.price = price
    
    def fillContainers (self,totalWeight):
        self.maxGramsInContainer = self.maxVolume * 29.5735296875
        if self.maxGramsInContainer > totalWeight/self.quantity:
            print("Container max Volume: "+str(self.maxGramsInContainer))
            print("Total Weight per container: " + str(totalWeight/self.quantity))
            print("Containers needed: "+ str(totalWeight/self.maxGramsInContainer) + '\n' )
            return totalWeight/self.maxGramsInContainer
            
        elif self.maxGramsInContainer < totalWeight/self.quantity:
            print("Container max Volume: "+str(self.maxGramsInContainer))
            print("Total Weight per container: " + str(totalWeight/self.quantity))
            print("Containers needed: "+ str(totalWeight/self.maxGramsInContainer)+ '\n' )
            return totalWeight/self.maxGramsInContainer
        else:
            print("Error for FillContainers in Candle CandleContainerClass")
            return None