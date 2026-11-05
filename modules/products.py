class Product:
    def __init__(self , id , name , brand , price , stock):
        self.__id = id
        self.name = name
        self.brand = brand
        self.__price = price
        self.__stock = stock

        if not isinstance(id, str) or not id.strip():
            raise ValueError("Invalid id format")

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Invalid name format")
        
        if not isinstance(brand, str) or not brand.strip():
            raise ValueError("Invalid brand format")
        
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Invalid price format")
        
        if not isinstance(stock, int) or stock < 0:
            raise ValueError("Invalid stock format")

    def getPrice(self):
        return self.__price

    def getId(self):
        return self.__id
    
    def setPrice(self, newPrice):
        if not isinstance(newPrice , (int, float)):
            raise ValueError("Invalid price format")
            
        elif newPrice <= 0:
            raise ValueError("Price value must be bigger than 0 ")

        else:
            self.__price = newPrice

    def getStock(self):
        return self.__stock

    def setStock(self, s):
        if not isinstance(s , int):
            raise ValueError("invalid stock format")

        elif s < 0:
            raise ValueError("Stock must be 0 or bigger")

        else:
            self.__stock = s

    def reduceStock(self , quantity):
        if not isinstance(quantity, int):
            raise ValueError("invalid format of quantity")

        elif quantity <= 0:
            raise ValueError("quantity must be bigger than 0")
        
        elif self.__stock - quantity < 0:
            raise ValueError(f"The currently available amount of this product ({self.name}) is {self.__stock}")

        else:
            self.setStock( self.__stock - quantity)

    def restock(self , quantity):
        if not isinstance(quantity, int):
            raise ValueError("invalid format of quantity")
        
        elif quantity <= 0:
            raise ValueError("quantity must be bigger than 0")

        else:
            self.setStock(self.__stock + quantity)

    def getInfo(self):
        attributes = list(self.__dict__.keys())
        values = list(self.__dict__.values())

        for i in range(len(attributes)):
            setIndex = 1 if len(attributes[i].split("__")) > 1 else 0
            cleanedAtrs = attributes[i].split("__")[setIndex]
            finalAtrs = "".join([" " + char.lower() if char.isupper() else char for char in cleanedAtrs])

            print(f"{i+1}. {finalAtrs}: {values[i]}")

    
class Phone(Product):
    def __init__(self, id, name, brand, price , stock , storage, batteryCapacity):
        super().__init__(id, name, brand, price , stock)
        self.storage = storage #storage in GB (Gigabyte)
        self.batteryCapacity = batteryCapacity

        if not isinstance(storage , int) or storage <=0:
            raise ValueError("invalid storage format")

        if not isinstance(batteryCapacity , int) or batteryCapacity <=0:
            raise ValueError("invalid battery capacity format")

    def calculateFinalPrice(self ,quantity):
        if not isinstance(quantity, int):
            raise ValueError("invalid quantity format")
        
        if quantity <= 0 :
            raise ValueError("Quantity must be bigger than 0")
        
        discount = 0
        if self.storage >= 256:
            discount = 0.05

        elif self.storage >= 512:
            discount = 0.08

        finalPrice = self.getPrice() * (1 - discount) * quantity
        return finalPrice

class Laptop(Product):
    def __init__(self, id, name, brand, price , stock, storage, ram , cpu):
        super().__init__(id, name, brand, price , stock)
        self.storage = storage
        self.ram = ram
        self.cpu = cpu
        
        if not isinstance(storage , int) or storage <=0:
            raise ValueError("invalid storage format")

        if not isinstance(ram , int) or ram <= 0 :
            raise ValueError("invalid ram size format")

        if not isinstance(cpu , str) or not cpu.strip():
            raise ValueError("invalid cpu name format")

    def calculateFinalPrice(self ,quantity):
        if not isinstance(quantity, int):
            raise ValueError("invalid quantity format")
        
        if quantity <= 0 :
            raise ValueError("Quantity must be bigger than 0")
        
        discount = 0
        if self.getPrice() >= 5000:
            discount = 0.10

        finalPrice = self.getPrice() * (1 - discount) * quantity
        return finalPrice


class Accessory(Product):
    def __init__(self, id, name, brand, price , stock, accessoryType, warranty ):
        super().__init__(id, name, brand, price , stock)
        self.accessoryType = accessoryType
        self.warranty = warranty #warranty in monthes

        if not isinstance(accessoryType, str) or not accessoryType.strip():
            raise ValueError("invalid accessory type format")

        if not isinstance(warranty , int) or warranty < 0 :
            raise ValueError("invalid warranty format")

    def calculateFinalPrice(self ,quantity):
        if not isinstance(quantity, int):
            raise ValueError("invalid quantity format")
        
        if quantity <= 0 :
            raise ValueError("Quantity must be bigger than 0")
        
        discount = 0                        
        if quantity > 3:
            discount = 0.15 


        finalPrice = self.getPrice() * (1 - discount) * quantity
        return finalPrice



