code1, unit1, price1 = input().split()
code1, unit1, price1 = int(code1), int(unit1), float(price1)
code2, unit2, price2 = input().split()
code2, unit2, price2 = int(code2), int(unit2), float(price2)


final_price = price1 * unit1 + price2 * unit2

print("VALOR A PAGAR: R$ %.2f" %final_price)