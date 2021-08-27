class fragranceClass:
    def __init__(self, gram, price, waxGrams,fragranceOilRatio):
        self.gram = gram
        self.price = price
        self.waxGrams = waxGrams
        self.fragranceOilRatio = fragranceOilRatio
    def oilUsedCalculate(self):
        return self.waxGrams*self.fragranceOilRatio
    def oilCalculate(self):
        oilGram = self.oilUsedCalculate()
        return oilGram* ( self.price/self.gram )
    