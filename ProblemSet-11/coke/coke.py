coins = [25, 10, 5]
price = 50
paid = 0

while True:
    print("Insert Coin")
    coin = int(input())
    if coin not in coins:
        print("Amount Due: 50")
    paid += coin
    if paid < price:
        print(f"Amount Due: {price - paid}")
    else:
        change = paid - price
        print(f"Change Owed: {change}")
        print("Thank you for your purchase!")
        break

if paid < price:
    print(f"Amount Due: {price - paid}")