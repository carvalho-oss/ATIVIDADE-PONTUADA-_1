import os
os.system ('cls')

print('''
====CDS ===

VERDE   | R$ 10.00
AZUL    | R$ 20.00
AMARELO | R$ 30.00
VERMELHO| R$ 40.00''')

cor = input('qual cor você deseja ?:).upper()

match cor:
    case 'verde':
        print('valor R$ 10.00')
    case 'Azul':
        print('valor R$ 20.OO')
    case 'AMARELO':
        print('valor R$30.00')
    case 'VERMELHO':
        print('valor 40.00')

    case:
        print('opção invalida')