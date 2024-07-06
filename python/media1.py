# ler duas notas
nota1 = float(input("Digite a primeira nota "))
nota2 = float(input("Digite a segunda nota "))
# calcular a média
media = (nota1 + nota2)/2
# verificar o conceito
if media >= 9:
    print("Conceito: O") 
elif media > 7 and media <= 8.9 :
    print("Conceito: B")
elif media > 5 and media <= 6.9:
    print("Conceito: S")    
else:
    print("Conceito: I")