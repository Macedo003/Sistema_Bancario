lista_compras = ['pão','manteiga','presunto','queijo','peito de peru','mortadela','reiquejão']

for indice,item in enumerate(lista_compras):
    print(indice,item)

while True:
    condicao =input('selecione uma opção \n [i]inserir [a]pagar [l]istar [f]echar ')
    condicao1 =condicao.lower().startswith('i')
    condicao2 =condicao.lower().startswith('a')
    condicao3 =condicao.lower().startswith('l')
    condicao4 =condicao.lower().startswith('f')

    if condicao1 is True:
        novo_item = input('Digite o nome do novo item: ')
        lista_compras.append(novo_item)
        print('O item foi adicionado com sucesso')
    if condicao2 is True:
        for indice,item in enumerate(lista_compras):
            print(indice,item)
        apagar_item = input('Digite o numero do indice do item que deseja apagar: ')
        try:
            apagar_item = int(apagar_item)
            del lista_compras[apagar_item]
            print('O item foi removido com sucesso')
            valor_valido = True
        except:
            valor_valido = None
        if valor_valido is None:
            print('Valor digitado é invalido')
            continue
        
    if condicao3 is True:
        print('A SUA LISTA ESTÁ AQUI!!!')
        for indice,item in enumerate(lista_compras):
            print(indice,item)


    if condicao4 is True:
        print('Voce Terminou a sua lista')
        break