cont = 1
while cont <5:
    nota = int(input("Digite uma nota entre 0 a 5:"))
    while nota <0 or nota >5:
        print ('nota invalida')
        nota = int(input("Digite uma nota entre 0 a 5"))
        i=i+5
print ("coleta finalizadas")        