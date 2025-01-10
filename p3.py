import json


with open("dados.json", "r") as file:
    data = json.load(file)

lowest = None
maximum = 0
total = 0
dias = 0
n_days_above_avg = 0

for entry in data:
    valor = entry["valor"]
    if valor > 0:
        if lowest is None or valor < lowest:
            lowest = valor
        maximum = max(valor, maximum)
        total += valor
        dias += 1

avg = total / dias if dias > 0 else 0
n_days_above_avg = sum(1 for entry in data if entry["valor"] > avg)

print(f"Menor faturamento registrado: {lowest:.2f}")
print(f"Maior faturamento registrado: {maximum:.2f}")
print(f"Faturamento medio: {avg:.2f}")
print(f"Dias com faturamento acima da media: {n_days_above_avg}")
