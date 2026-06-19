stocks = {
    "AApl" : 180,
    "TSLA" : 250,
    "GOOG" : 150
    
}

stock = input("Enter stock name:").upper()
quantity = int(input("Enter quantity:"))

if stock in stocks:
    total = stocks[stock] * quantity
    print("Total Investment =", total)
    
else:
    print("stock not found!")