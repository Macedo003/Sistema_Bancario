

while True:
    n1 = input('Digite o primeiro Numero: ')
    n2 = input('Digite o segundo Numero: ')
    operador = input('Digite o operador (+-/*)')

    numeros_validos = None

    try:
        num_1_float = float(n1)
        num_2_float = float(n2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um dos numeros digitados são invalidos')
        continue

    operadores_validos = '+-/*'
    if operador not in operadores_validos:
        print('Voce digitou um operador invalido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    operador_soma = '+'
    operador_sub = '-'
    operador_div = '/'
    operador_mult = '*'

    if operador in operador_soma:
        soma = num_1_float + num_2_float
        print('A soma entre {} e {} é igual a {}'.format(num_1_float,num_2_float,soma))
    elif operador in operador_sub:
        sub = num_1_float - num_2_float
        print('A subtração entre {} e {} é igual a {}'.format(num_1_float,num_2_float,sub))
    elif operador in operador_div:
        div = num_1_float / num_2_float
        print('A divisão entre {} e {} é igual a {}'.format(num_1_float,num_2_float,div))
    elif operador in operador_mult:
        mult = num_1_float * num_2_float
        print('A multiplicação entre {} e {} é igual a {}'.format(num_1_float,num_2_float,mult))
    

    sair = input('Quer sair? [s]im: ')
    sair = sair.lower().startswith('s')
    
    if sair is True:
        break