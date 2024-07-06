# ler o  nome so usuário
# strip retira espaços m branco no início e no final da string
# title altera todas as  primeiras letras da variável para maiúscula
nome = input("Qual é o seu nome? ").strip().title()
primeiro, sobrenome = nome.split(" ")
# exibir uma mensagem na tela de saudação
print(f"Olá, {nome}")
print(sobrenome)