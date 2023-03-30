cpf = '74682489070'
nove_digitos = cpf[:9]
cont_regre_1 = 10

resultado_digito_1 = 0

for digito in nove_digitos:
    resultado_digito_1 +=int(digito) * cont_regre_1
    cont_regre_1 -= 1
digito_1 = ((resultado_digito_1 *10) %11)
digito_1 = digito_1 if digito_1 <= 9 else 0


dez_digitos = nove_digitos + str(digito_1)
cont_regre_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito)*cont_regre_2
    cont_regre_2 -= 1
digito_2=((resultado_digito_2*10)%11)
digito_2 = digito_2 if digito_2<=9 else 0

novo_cpf = '{}{}{}'.format(nove_digitos,digito_1,digito_2)

if cpf == novo_cpf:
    print('{} é valido'.format(novo_cpf))
else:
    print('CPF invalido')
