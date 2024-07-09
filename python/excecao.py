# Exceptions
# try
# except

try:
    x = int(input("Digite um valor para x "))
    print(f"x é {x}")
except ValueError:
    print("x não é um número")
