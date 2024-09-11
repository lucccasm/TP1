# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).
import math
battery_level = float(input("Pourcentage de batterie ?"))
if battery_level ==0:
    print(" La batterie est vide")
distance= 0

while battery_level > 0:
    if 50< battery_level <= 100:
        distance+= (battery_level-50)*2
        battery_level = 50

    if 25< battery_level <= 50:
        distance+= float((battery_level-25)*0.5)
        battery_level = 25
    if 10< battery_level <= 25:
        distance+= (battery_level-10)*1
        battery_level = 10

    if 5< battery_level <= 10:
        distance+= float((battery_level-5)*2.5)
        battery_level = 5

    if 0< battery_level <= 5:
        distance+= battery_level*6
        battery_level=0

    print(f" {distance} km")
