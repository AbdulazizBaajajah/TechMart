import os
from products import Laptop, Phone , Accessory

currentDirPath = os.path.dirname(os.path.abspath(__file__))
productsFile = os.path.abspath(os.path.join(currentDirPath , "../data/products.txt"))

def cleanData(l):
    cleanedData = []
    for d in l:
        if "." in d:
            try:
                cleanedData.append(float(d))

            except ValueError:
                cleanedData.append(d)

        elif d.isdecimal():
            cleanedData.append(int(d))

        else: cleanedData.append(d)

    return cleanedData

def loadProducts():
    productsList = []
    with open(productsFile , "r") as file:
        data = file.read()
        productsSplit = data.split("\n")
        
        for p in productsSplit:
            productSplit = p.split("|")
            match productSplit[0]:
                case "Laptop":
                    productsList.append(Laptop(*cleanData(productSplit[1:])))

                case "Phone":
                    productsList.append(Phone(*cleanData(productSplit[1:])))

                case "Accessory":
                    productsList.append(Accessory(*cleanData(productSplit[1:])))

    return productsList

def saveProducts(products):
    infoString = ""
    for i in range(len(products)):
        product = products[i]
        productInfo = [str(n) for n in list(product.__dict__.values())]
        productType = product.__class__.__name__
        productInfo.insert(0 , productType)
        infoString += "|".join(productInfo) + "\n"

    with open(productsFile , "w") as file:
        file.write(infoString)

productsList = loadProducts()

for p in productsList:
    print(type(p).__name__)
    p.getInfo()
    print()
    