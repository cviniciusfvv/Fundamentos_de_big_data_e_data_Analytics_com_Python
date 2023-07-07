v1 = float (input("Digire o preço do carro ano de 2021"))
v2 = float (input("Digire o preço do carro ano de 2022"))
v3 = float (input("Digire o preço do carro ano de 2023"))
if v1 > v2 and v1 > v3:
    print(f"o preço {v1}é o maior valor de veiculo")
    if v2<v3:
        print(f"o preço {v2}é o menor valor de veiculo")
    elif v3<v2:
        print(f"o preço {v3}é o menor valor de veiculo")
elif v2 > v1 and v2 > v3:
    print(f"o preço {v2}é o maior valor de veiculo")
    if v1<v3:
        print(f"o preço {v1}é o menor valor de veiculo")
    elif v3<v1:
        print(f"o preço {v3}é o menor valor de veiculo")
elif v3 > v1 and v3 > v1:
    print(f"o preço {v3}é o maior valor de veiculo")
    if v1<v2:
        print(f"o preço {v1}é o menor valor de veiculo")
    elif v2<v1:
        print(f"o preço {v2}é o menor valor de veiculo")