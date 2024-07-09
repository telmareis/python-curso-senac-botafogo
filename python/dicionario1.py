personagens = [
                {
                "nome": "Frodo","especie": "Hobbit","local": "Condado",
                },
                {
                "nome": "Sam","especie": "Hobbit","local": "Condado",
                },
                {
                "nome": "Legolas","especie": "Elfo","local": "Valfenda",
                },
              ]       


for personagem in personagens:
    print(personagem["nome"], personagem["local"])