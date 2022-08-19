#METHOD-1

def price(item, cost):
    return "The " + item + " costs $" + str(cost) + "."

print(price("chair", 40.99))
print(price("book", 12.84))
print(price("soap", 3.95))

#METHOD-2

def price(item, cost):
    print( "The " + item + " costs $" + str(cost) + ".")

price("chair", 40.99)
price("book", 12.84)
price("soap", 3.95)
