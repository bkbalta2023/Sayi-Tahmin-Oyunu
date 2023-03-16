import random
import time

print("""

SAYI TAHMİN OYUNU

1 ile 10 arasında sayıyı tahmin edin.

Tahmin hakkiniz 3


""")

sayimiz = random.randint(1,10)
tahminhakki = 3
while True:
    tahmin = int(input("Tahmininiz: "))

    if tahmin != sayimiz :

        tahminhakki -= 1

        print("Yanlis")
        if tahminhakki == 0:
            print("Tahmin hakkiniz doldu")
            break

    else:
        print("Dogru!")
        break


