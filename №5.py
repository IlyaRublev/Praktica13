sata ={}
with open("sata.txt", "r") as file:
    for i in file:
        a, b, c = i.strip().split()
        key = (a, b)
        if key in sata:
            sata[key] += int(c)
        else:
            sata[key] = int(c)
for key, d in sata.items():
    a, b = key
    print(f"Покупатель: {a},Товар:{b},Количество:{d}")