
st = "90,45,66,79,10,92"
parts = st.split(",")
# convert str in list to int
prices = [int(s) for s in parts]

print('Min Price  :', min(prices))
print('Max Price  :', max(prices))
print(f'Avg Price  : {sum(prices) / len(prices):.2f}')
