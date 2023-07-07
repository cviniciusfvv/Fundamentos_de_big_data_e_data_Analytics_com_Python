Combustivel= input('Escolha o combustivel desejado G, E ou D:')
litros= int(input(" Quantos litros você quer abastecer:"))

if Combustivel == 'E' and litros < 15:
    total = (1.70 * litros)
    vp= total - (total*0.02)
    print(f" o Valor a ser pago do combustivel sem desconto é R$", total)
    print(f" o Valor a ser pago do combustivel com desconto é R$", vp)

if Combustivel == 'E' and litros >= 15:
    total = (1.70 * litros)
    vp= total - (total*0.04)
    print(f" o Valor a ser pago do combustivel sem desconto é R$", total)
    print(f" o Valor a ser pago do combustivel com desconto é R$", vp)

if Combustivel == 'D' and litros < 20:
    total = (2 * litros)
    vp= total - (total*0.03)
    print(f" o Valor a ser pago do combustivel sem desconto é R$", total)
    print(f" o Valor a ser pago do combustivel com desconto é R$", vp)

if Combustivel == 'D' and litros >= 20:
    total = (2 * litros)
    vp= total - (total*0.05)
    print(f" o Valor a ser pago do combustivel sem desconto é R$", total)
    print(f" o Valor a ser pago do combustivel com desconto é R$", vp)

if Combustivel == 'G' and litros < 20:
    total = (4.5 * litros)
    vp= total - (total*0.03)
    print(f" o Valor a ser pago do combustivel sem desconto é R$", total)
    print(f" o Valor a ser pago do combustivel com desconto é R$", vp)

if Combustivel == 'G' and litros >= 20:
    total = (4.5 * litros)
    vp= total - (total*0.04)
    print(f" o Valor a ser pago do combustivel sem desconto é R$", total)
    print(f" o Valor a ser pago do combustivel com desconto é R$", vp)