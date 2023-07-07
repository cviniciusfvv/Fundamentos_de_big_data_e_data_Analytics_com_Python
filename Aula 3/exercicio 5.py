protuto1 = float (input("Digire o preço produto1:"))
v2 = float (input("Digire o preço produto2:"))
v3 = float (input("Digire o preço produto3:"))
if protuto1 < v2 and protuto1 < v3:
    print(f"o preço {protuto1}é o menor valor de produto")
elif v2 < protuto1 and v2 < v3:
    print(f"o preço {v2}é o menor valor de produto")
elif v3 < protuto1 and v3 < protuto1:
    print(f"o preço {v3}é o menor valor de produto")