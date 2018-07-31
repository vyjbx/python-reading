'''
Here we use a bank account demo to show how descriptors work. Descriptors provide a lower level connection and interface to an instance's properties. Note property is a special use case of descriptors. 

Begins with the popular temperature example.
'''

class Fe(object):
    def __get__(self, instance, owner):
        return instance.value
    def __set__(self, instance, value):
        instance.value = value
class Ce(object):
    convert_rate = 1.8
    offset = 10
    def __get__(self, instance, owner):
        return (instance.value - self.offset)*self.convert_rate
    def __set__(self, instance, value):
        instance.value = value/self.convert_rate + self.offset
    @classmethod
    def set(cls, offset):
        cls.offset = offset
        
class Temperature(object):
    F = Fe()
    C = Ce()
    def __init__(self, temp=0):
        self.value = temp



'''
The bank demo follows

Here instead of defining the currency classes one by one, we notice they have the exactly same templates. We create a super class Money first 
'''
class Money(object):
    rate = 1.0
    name = 'usd'
    def __init__(self):
        self.transaction_fee = 0.0
    def __get__(self, instance, owner):
        return instance.balance * self.rate
    def __set__(self, instance, value):
        instance.balance = value / self.rate
    
    @classmethod
    def set_name(cls, name):
        cls.name = name
    @classmethod
    def set_rate(cls, rate):
        cls.rate = rate

'''
We can inherate from Money to create individual currencies, such as 
'''
class USD1(Money):
    def __init__(self, name, rate):
        self.set_name(name)
        self.set_rate(rate)

class CND1(Money):
    def __init__(self, name, rate):
        self.set_name(name)
        self.set_rate(rate)

'''
Or, instead we can use a class factory to generate these difference classes utilizing the __call__ method
'''

class Currency(object):
    def __call__(self, name, rate):
        class X(Money):
            pass
        X.set_name(name)
        X.set_rate(rate)
        return X

'''
The new class can be created as
'''
currency_factory = Currency()
USD2 = currency_factory('USD', 1.0)
CND2 = currency_factory('CND', 1.3)
EURO2 = currency_factory('EURO', 0.8)

'''
Now the over simplified account model is defined as 
'''
class Balance(object):
    usd = USD2()
    cnd = CND2()
    euro = EURO2()
    def __init__(self, user_id, balance=0.0):
        self.user_id = user_id
        self.balance = balance


account = Balance(10001, 1000.0)
print account.cnd

'''
And we can change the exchange rate 
'''
CND2.set_rate(1.5)
print account.cnd


'''
Now as we have many (3) currencies, it is necessary to have something to manage these currencies. We can use again another over simplified class as currency warehouse to manage the currencies.

Two methods add_currency and set_rate will add a currency class in the warehouse, and change the exchange rate by calling the class method on the class.
'''
class Currency_Manager(object):
    def add_currency(self, C):
        setattr(self, C.name, C)
    def set_rate(self, name, rate):
        getattr(self, name).set_rate(rate)

C_manager = Currency_Manager()
C_manager.add_currency(USD2)
C_manager.add_currency(CND2)
C_manager.add_currency(EURO2)

'''
Now we can change the currency rate in warehouse. It has all the currencies we use and is the one interface we can edit those classes.
'''

C_manager.set_rate('CND', 1.8)
print account.cnd














