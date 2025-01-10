# Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado: 
# •	SP – R$67.836,43 
# •	RJ – R$36.678,66 
# •	MG – R$29.229,88 
# •	ES – R$27.165,48 
# •	Outros – R$19.849,53 

fat = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(fat.values())

print(f"Total: R${total:.2f}")

for estado, valor in fat.items():
    percent = (valor / total) * 100
    print(f"{estado}: {percent:.2f}%")

