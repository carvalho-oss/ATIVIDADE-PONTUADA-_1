import os
os.system ('cls')

('''
fruta = 5kg | acima de 5kg
morango = 2.50 por kg | acima 2.20 por kg
maca = 1.80 por kg | acima 1.50 por kg
''')
morango = float(input(" Digite a sua quantidade de morango em Kg: "))
maca = float(input(" Digite a sua quantidade de maca em Kg: "))
# Preço do morango

if morango <=5:
    preco = morango * 2.50
else:
    valor_morango =  2.20

# Preço da maçã

if maca <=5:
    preco = maca * 1.80
else:
    valor_maca =  1.50


# Somando quantidades

quantidade_total = morango + maca

# Somando valores

total = valor_morango + valor_maca

# Verificando desconto

if quantidade_total >= 10:
    desconto = total * 0.10
    valor_final = total - desconto
    print(" desconto de 10% aplicado")
    print(f" valor do desconto: R$ {desconto}")

