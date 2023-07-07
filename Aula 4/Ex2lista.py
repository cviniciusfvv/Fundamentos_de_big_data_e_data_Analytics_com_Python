cont =0 
gastos_lista = [2172.52, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45,
3075.36, 2317.64, 3219.08]
for gastos in gastos_lista:
    if gastos >3000:
        cont= cont+1
print(f"Gastos acima de 3000: {cont}")
porc=(cont/len(gastos_lista) *100)
print(f"Porcentagem de gastos acima de 3000 {porc} %")