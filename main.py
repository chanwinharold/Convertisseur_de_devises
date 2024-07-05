from modules.functions import choixFonction

#Liste des devises
print("\n***Convertisseur de devises ©2024***\n")
print("1-Euro\t2-Dollar US\n3-Livre\t4-Yuan\n5-Fcfa\t6-Yen\n")

#L'utilisateur choisi la devise d'entrée
choix1 = int(input("Choisissez une devise en entrée dans la liste ci-dessus: "))
while (choix1 not in [1, 2, 3, 4, 5, 6]):
    choix1 = int(input("Choisissez une devise en entrée dans la liste ci-dessus: "))

#L'utilisateur choisi la devise de sortie
choix2 = int(input("Choisissez une devise en sortie dans la liste ci-dessus: "))
while (choix2 not in [1, 2, 3, 4, 5, 6] or choix1 == choix2):
    choix2 = int(input("Choisissez une devise en entrée dans la liste ci-dessus: "))

#Ceci servira lors de l'affichage du résultat final
devises = ["", "Euros", "Dollars US", "Livres Sterling", "Yuan", "Fcfa", "Yen"]
devise1 = devises[choix1]
devise2 = devises[choix2]

#L'utilisateur entre le montant à convertir
montant = float(input("\nEntrez le montant à convertir: "))

#On affiche le résultat final
résultat = choixFonction.choixFonction(choix1, choix2, montant)
print(f"\n{montant} {devise1} = {résultat} {devise2}")

