# Take price and display net price after a discount of 20%
# and tax of 12%

price = int(input("Enter price :"))
discount = price * 20 // 100
after_discount = price - discount
tax  = after_discount * 12 // 100
net_price = after_discount + tax

print(f'Price           : {price:6}')
print(f'-Discount       : {discount:6}')
print(f'After Discount  : {after_discount:6}')
print(f'+ Tax           : {tax:6}')
print(f'Net Price       : {net_price:6}')

