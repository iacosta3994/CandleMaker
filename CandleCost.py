from typing import Container
from Classes.waxClass import waxClass
from Classes.wickClass import wickClass
from Classes.candleContainerClass import candleContainerClass
from Classes.addonClass import addonClass
from Classes.dyeClass import dyeClass
from Classes.fragranceClass import fragranceClass

#type,weight g,price $
wax = waxClass('soy', 4535.92, 31.95) 
#type,quantity, price $
wick = wickClass('wood', 100, 13.99)
#maxVolume fl oz,quantity, price $
container = candleContainerClass(8, 24, 36.99)
#type, weight g, price$
addon = addonClass('lavender', 453.592,  13.95)
#grams ,price, wax weight, Dye percentage
dye = dyeClass(56.699, 18.84, wax.weight, 0.00375)
#gram, price, wax in grams, 
fragrance = fragranceClass(453.592, 52.99, wax.weight, .1)


class Candle:
    def __init__(self, wax, wick, container, addon, dye, fragrance):
        self.wax = wax
        self.wick = wick
        self.container = container
        self.addon = addon
        self.dye = dye
        self.fragrance = fragrance
        self.costOfDye = self.dye.dyeCalculate()
        self.dyeUsed = self.dye.dyeUsedCalculate()
        self.costOfFragranceOil = self.fragrance.oilCalculate()
        self.oilUsed = self.fragrance.oilUsedCalculate()
        self.totalWeight = self.getWeight()
        self.totalPrice = Candle.getPrice(self)
        self.containerNeeded = Candle.getContainersNeeded(self)


    def getPrice(self):
        return (self.wax.price + 
                self.wick.price +
                self.container.price +
                self.addon.price +
                self.costOfDye+ 
                self.costOfFragranceOil)
    def getWeight(self):
        return (self.wax.weight +
                self.addon.weight +
                self.dyeUsed+
                self.oilUsed)
    def getContainersNeeded(self):
        return self.container.fillContainers(totalWeight = Candle.getWeight(self))

  
    

    def printPrice(self):
            print('Cost of ' + str(self.wax.type) + ' candle at ' + str(self.wax.weight) + ' grams is $' + str(self.wax.price))
            print('Cost of ' + str(self.wick.type) + 'wick is ' + str(self.wick.price))
            print('Cost of container is $' + str(self.container.price))
            print('Cost of addons is $' + str(self.addon.price))
            print('Cost of dye for ' + str(self.wax.weight) + 'grams of wax is $' + str(round(self.costOfDye,2)) + " using " + str(self.dyeUsed) +  " grams of dye.")
            print('Cost of oil for ' + str(self.wax.weight) + 'grams of wax is $' + str(round(self.costOfFragranceOil,2)) + " using " + str(self.oilUsed) +  " grams of fragrance oil.")
            print('Individual cost for one of the '+ str(round(self.containerNeeded, 2)) + ' candle(s) is: $' + str(round(self.totalPrice / self.containerNeeded , 2)))
            

    def __str__(self):
        return '\nCost: $' + str(Candle.getPrice(self)) + '\nTotal Weight in Grams: ' + str(Candle.getWeight(self) ) 


lavenderCandle = Candle(wax, wick, container, addon, dye, fragrance)

lavenderCandle.printPrice()

print(lavenderCandle)
