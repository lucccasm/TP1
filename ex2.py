# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.
import math

water_quantity = input("Quelle quantité d'eau faut-il assainir ? ")

filtres = math.ceil(float(water_quantity)/5)

lampes = math.ceil(float(water_quantity) * 0.6)

chlore= float(water_quantity)/10


print(f"Voici les éléments requis pour assainir {water_quantity}L d'eau:\n")
print("        	- Filtre(s) :", filtres)
print("\n        	- Lampe(s) UV :", lampes,)
print(f"\n        	- Chlore : {chlore}kg")





