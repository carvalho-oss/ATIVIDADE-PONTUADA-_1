import os
os.system ('cls')

print('''
=== Posto de combustível
Combustível  | Quantidade de Vendas | Desconto por litro
Álcool       |  Até 25 litros       | 10%
Álcool       | Acima de 25 litros   |20%
Gasolina     | 25 litros            |15%
Gasolina     | acima de 25 litros   | 30%''')

combustível = input('\n ALCOOL OU GASOLINA?: ').upper()
quantidade = int(input('Quantos litros ?: '))

if combustível == 'ALCOOL'and quantidade <= 25:
    preco = (3.79 * quantidade) * 0.10
elif combustível == 'ALCOOL'and quantidade >= 25:
    preco = (3.79 * quantidade) * 0.20

elif combustível == 'ALCOOL' and quantidade <= 25:
    preco (6.59 * quantidade) * 0.20
elif combustível == 'GASOLINA' and quantidade <= 25:
    preco = (3.79 * quantidade) * 0.15
elif combustível == 'GASOLINA' and quantidade >= 25:
    preco = (6.59 * quantidade) * 0.3

else:
        print('nada a declarar')

print (' você pediu: {combustível}: e o seu preço foi {preco}')