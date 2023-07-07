n1 = float(input('Digite o primeiro numero'))
n2 = float(input('Digite o segundo numero'))
op = input(' Escolha a operação desejada +,-,*,/')
if op == '+':
    res = n1 + n2
    print(f'A soma de {n1} e {n2} = {res}')
elif op == '-':
    res = n1 - n2
    print(f'A Subtração de {n1} e {n2} = {res}')
elif op == '*':
    res = n1 * n2
    print(f'A multipliacação de {n1} e {n2} = {res}')
else:
    if n2 ==0:
        print(' O valor da divisão por 0 não é possivel')
    else:
        res = n1/n2
        print(f'A Divisão de {n1} e {n2} = {res}')