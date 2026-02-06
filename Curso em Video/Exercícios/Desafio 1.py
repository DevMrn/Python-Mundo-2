# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input("Qual o valor da casa? R$ "))
salario = float(input("Qual o salário do comprador? R$ "))
anos = int(input("Em quantos anos pretende pagar? "))

valorParcela = valorCasa / (anos * 12)
limite = salario * 0.30

if valorParcela <= limite:
    print("Empréstimo APROVADO!")
else:
    print("Empréstimo NEGADO!")

print(f"Parcela mensal: R$ {valorParcela:.2f}")
print(f"Limite permitido: R$ {limite:.2f}")
