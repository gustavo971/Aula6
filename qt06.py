"""Exercício 6: Escreva um programa que peça ao usuário para digitar uma palavra e, 
em seguida, imprima a palavra ao contrário utilizando um loop "for"."""

palavra = input("Digite uma frase")

#for letra in palavra[::-1]:
    #print(letra)
for letra in reversed(palavra):
    print(letra)
