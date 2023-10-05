def main():
    coke = 50
    total_paid = 0
    coins = [25,10,5]

    while coke > 0:
        print(f"Amount Due: {coke}")
        pay = int(input("Insert Coin: "))
        if pay in coins:
            coke = coke - pay
            total_paid = total_paid + pay
    if total_paid >= coke:
        print(f"Change Owed: {total_paid-50}")

main()