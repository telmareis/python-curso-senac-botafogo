personagens = ["Frodo", "Sam", "Aragorn","Gandalf"]

especies = ["Hobbit", "Hobbit", "Homem", "Mago"]

lista_intercalada = [personagens + especies]
for item1, item2 in zip(personagens, especies):
    lista_intercalada.append(item1)
    lista_intercalada.append(item2)
print(lista_intercalada)