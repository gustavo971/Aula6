"""Exercício 2: Escreva um programa que peça ao usuário para digitar um número e,
 em seguida, imprima a tabuada desse número (de 1 a 10) utilizando um loop "for"."""

n = int(input("digite um numero"))

for x in range (1,11):
        print(f'{n} x {x} = {n * x}')
    