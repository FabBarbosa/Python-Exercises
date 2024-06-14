a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

maiorAB = (a + b + abs(a - b))/2
maiorABC = (maiorAB + c + abs(maiorAB - c))/2
maiorABC = int(maiorABC)

print(f"{maiorABC:,.0f} eh o maior")