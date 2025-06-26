money = str(input("Введите цену: "))
if "." not in money:
    money = money + ".00"
rub, kop = money.split(".")
total_kop = int(rub) * 100 + int(kop)
denominations = [
    ("5000₽", 5000*100), ("2000₽", 2000*100), ("1000₽", 1000*100),
    ("500₽", 500*100), ("200₽", 200*100), ("100₽", 100*100), ("10₽", 10*100),
    ("5₽", 5*100), ("2₽", 2*100 ), ("1₽", 100),
    ("1коп.", 1)
]

for num in denominations:
    if total_kop // num[1] > 0:
        if total_kop//num[1] > 0:
            count = 0
            for i in range(total_kop//num[1]):
                total_kop = total_kop - num[1]
                count += 1
            print(f"{num[0]} x {count}")

