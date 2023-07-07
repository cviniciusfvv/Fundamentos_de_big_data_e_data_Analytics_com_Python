lista = ["Daniel", "Senai", 0,10,25,30,40]
lista.append(52)
lista.remove(25)
lista.remove(lista[0])
print(lista)
print(f"Ultimo elemento da lista:{ lista[len(lista)-1]}")
print(f"Ultimo elemento da lista:{ lista[4]}")
lista_numeros=[10,20,30,40]
soma = sum(lista_numeros)
media = sum(lista_numeros)/(len(lista_numeros)-1)
print(f"Soma dos valores da lista: {soma}")
print("Media dos valores da lista: %.2f"%(media))
for i in lista:
    if "A" in lista:
        print(f"Senai")
    else:
        print(f"Senai não está na lista")
  
