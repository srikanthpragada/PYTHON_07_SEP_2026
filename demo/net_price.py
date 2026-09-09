# Take price and display net price after a tax of 10%

data = input("Enter price :")
price = int(data)   # Convert str to int
tax = price * 10 // 100
net_price = price + tax
print('Net Price :', net_price)

