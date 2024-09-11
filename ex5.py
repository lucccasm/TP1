#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country = input("Pays concerné ? ")
code_medals = input("Chaine représentant les médailles ? ")
Gold = 0
Silver = 0
Bronze = 0
for lettre in code_medals:
    if lettre == "G":
        Gold += 1
    if lettre == "S":
        Silver += 1
    if lettre == "B":
        Bronze += 1


print(country + ":")
print("-", Gold, "OR")
print("-", Silver, "Argent")
print("-", Bronze, "Bronze")
