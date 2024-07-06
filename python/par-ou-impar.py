def par_ou_impar(numero): 
    if numero % 2 == 0: 
        return "O número é par." 
    else: 
        return "O número é ímpar."

numero = int(input("Digite um número: ")) 
resultado = par_ou_impar(numero)
print(resultado)
