class dyeClass:
    def __init__(self,grams,price, waxGrams, dyeRatio):
        self.grams = grams
        self.price = price
        self.waxGrams = waxGrams
        self.dyeRatio = dyeRatio
    def dyeUsedCalculate(self):
        return self.waxGrams * self.dyeRatio
    def dyeCalculate(self):
        dyeGram = self.dyeUsedCalculate()
        return dyeGram * (self.price/self.grams )

