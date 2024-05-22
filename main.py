#Crie um programa que solicite ao usuário um número e exiba a soma de todos os seus dígitos
numero = input("Digite um número: ")

soma = 0

for i in numero:
    if i.isdigit():
        soma += int(i)

print("A soma de todos os dígitos é:", soma)