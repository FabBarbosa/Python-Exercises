A, B, C = map(float, input().split())

DELTA = B ** 2 - 4 * A * C

if A == 0 or B == 0 or C == 0 or DELTA < 0:
    print('Impossivel calcular')

else:
    print("R1 = %.5f" % ((-1 * B + DELTA ** 0.5) / (2 * A)))
    print("R2 = %.5f" % ((-1 * B - DELTA ** 0.5) / (2 * A)))