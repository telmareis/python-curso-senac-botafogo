nome = input("Digite o personagem ")

match nome:

    case "Frodo":
        print("Hobbit")
    case "Sam":
        print("Hobbit") 
    case "Aragorn":
        print("Homem")
    case "Gandalf":
        print("Mago") 
    case _:
        print("Quem???")