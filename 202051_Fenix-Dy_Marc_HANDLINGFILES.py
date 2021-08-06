products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}


# CODE CELL
def get_product(code):
    try:
        return products[code]
    except:
        return "Invalid Input"


# PROBLEM 1
print(get_product("americano"))
print(get_product("america"))
print(get_product(1))
print(get_product(True))


# CODE CELL
def get_property(code,property):
    try:
        return products[code][property]
    except:
        return "Invalid Input"

# PROBLEM 2
print(get_property("espresso","price"))
print(get_property("espress","o"))
print(get_property(1,True))
print(get_property('espresso','name'))

# CODE CELL

def main():
    try:
        product, quantity = input("{product_code},{quantity} ").split(",")
        c
    
    except:
        print("End Session")
    
        


# PROBLEM 3
print(main())

