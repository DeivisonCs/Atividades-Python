# 4) Faça um programa que recebe uma string do usuário e informa se ela é um palíndromo.
# Um palíndromo é uma frase que, excluindo os espaços em branco, pode ser lida
# indiferentemente da esquerda para a direita e da direita para a esquerda. Alguns
# palíndromos conhecidos são: ovo, radar, a grama é amarga, a base do teto desaba.

text = input("Digite algo: ")
no_spaces_text = text.replace(' ', '')
answer = "É um palíndromo"

for i in range(len(no_spaces_text)//2):

    if(no_spaces_text[i] != no_spaces_text[len(no_spaces_text)-i-1]):
        answer = "Não é um palindromo"

print(answer)