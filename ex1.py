# TODO: Créer un script permettant le formattage du livre des records des JO.

pays = input("De quelle nationalité est l'athlète ? ")
athlete = input("Quel est son nom ? ")
date = input("Date du record ? ")
disipline = input("Dans quelle discipline ? ")
categorie = input("Dans une catégorie spécifique ? ")
record = input("Quel est le record ? ")

print("\nNouveau Record:")
print("--------------------")
print(date, "-", disipline, "-", categorie + ":")
print("\t" + athlete, "(" + pays + ")", "-", record)