# Cheung Kai Cun Ronald, 202670M , IT2153-02
class Stock:
    count = 0
    def __init__(self,index,desc,price,level,amount,expDate):
        Stock.count += 1
        if Stock.count > 20:
            raise TypeError
        self.__index = index
        self.__desc = desc
        self.__price = price
        self.__level = level
        self.__amount = amount
        self.__expDate = expDate

    def get_index(self):
        return self.__index + 1

    def get_desc(self):
        return self.__desc

    def get_price(self):
        return self.__price

    def get_level(self):
        return self.__level

    def get_amount(self):
        return self.__amount

    def get_expDate(self):
        return self.__expDate

    def set_desc(self,desc):
        self.__desc = desc

    def set_price(self,price):
        self.__price = price

    def set_level(self,level):
        self.__level = level

    def set_amount(self,amount):
        self.__amount = amount

    def set_expDate(self,expDate):
        self.__expDate = expDate

    def __str__(self):
        return 'Index {}\nDescription: {}\nPrice: ${}\nStock Level: {}\nAmount: {}\nDays till expiry date: {} day(s)'\
            .format(self.__index + 1,self.__desc,self.__price,self.__level,self.__amount,self.__expDate)
