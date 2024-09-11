# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.
import math
speed = input("Vitesse initiale (m/s): ")
angle = input("Angle de lancer (en degrés): ")

g = 9.8
D = (math.pow(float(speed), 2) * math.sin(2 * math.radians(float(angle))))/g
print("Distance parcourue:", str(round(D, 2)) + "m")