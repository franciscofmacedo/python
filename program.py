#Desenvolva um programa em Python que leia o primeiro nome de uma pessoa e seu salário do mês de abril e na sequência mostre uma mensagem formatada
# . Exemplo, se o nome que a pessoa digitou foi "João" e o salário foi de 1000 reais,  a mensagem deve ser a seguinte: "O salário de João no mês 
# de abril foi de R$1.000,00 reais". Suponha que o usuário digitará apenas números para representar o salário e apenas letras para representar o
#  nome.

nome = input("Nome: ")

salário = input("Salário do mês de abril: ")

Inform = "O salário de" + " . " + nome + " . " + "no mês de abril foi de R$"  + salário + ",00 reais"

print(Inform)
