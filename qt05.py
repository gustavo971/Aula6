'''Exercício 5: Escreva um programa que peça ao usuário para digitar uma frase e, em seguida,
 conte quantas vogais (a, e, i, o, u) existem na frase utilizando um loop "for".'''

frase = input("Digite uma frase")
total_a, total_e, total_i, total_o,total_u = 0,0,0,0,0

for letra in frase:
    

    if letra == "a":
        total_a += 1
    elif letra == "e":
        total_e += 1
    elif letra == "i":
        total_i += 1
    elif letra == "o" :
        total_o += 1
    elif letra == "u":
        total_u += 1


print("O total de vogais é a:", total_a)
print("O total de vogais é e:", total_e)
print("O total de vogais é i:", total_i)
print("O total de vogais é o:", total_o)
print("O total de vogais é u:", total_u)




