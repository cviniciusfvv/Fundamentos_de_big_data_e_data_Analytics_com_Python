imoveis2022 = int(input("Digite Imoveis vendidos em 2022:"))
imoveis2023 = int(input("Digite Imoveis vendidos em 2023:"))

total = ((imoveis2023 - imoveis2022)/imoveis2022) * 100
print(total)

if total >20:
    print("Bonificação para o time de vendas")
elif total >2 and total<= 20:
    print("pequena bonificação para o time de vendas")
elif total >-10 and total < 2:
    print("Reajuste na politica de vendas")
else:
    print('corte de gasto')