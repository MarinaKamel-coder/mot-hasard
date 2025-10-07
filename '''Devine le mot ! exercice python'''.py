'''Devine le mot ! exercice python'''
# dessins_pendu est une liste de dessins qui représente l'état du pendu en fonction du nombre d'essais restants
dessins_pendu = [
    """
      +---+
      |   |
          |
          |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      |   |
          |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      |   |
      O   |
          |
          |
          |
          |
    ========
    """,
    """
      +---+
      |   |
      |   |
      O   |
     /    |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      |   |
      O   |
     /|   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      |   |
      O   |
     /|\\  |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      |   |
      O   |
     /|\\  |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      |   |
      O   |
     /|\\  |
      |   |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      |   |
      O   |
     /|\\  |
      |   |
     / \\  |
    PERDU!|
    =========
    """
    ]

import random

# Choisir un mot au hasard
mots = ["python", "programmation", "ordinateur", "developpeur"]
mot_secret = random.choice(mots)

# Initialiser les variables
lettres_essayees = []  # On stocke toutes les lettres tentées (trouvées ou ratées)
lettres_trouvees = [] # Liste pour stocker les lettres trouvées
essais_restants = 8

#fonction pour vérifier si l'utilisateur a entré 'exit'
def verifier_sortie(entree: str): 
    if entree.lower() == 'exit':
        print("Merci d'avoir joué !")
        exit(0)

# Début du jeu
print("Bienvenue au jeu du Pendu !")

# Boucle de jeu
while essais_restants > 0:
    affichage_du_mot = "" # On affiche le mot à afficher avec des _
    for lettre in mot_secret: #lettre est une variable qui prend la valeur de chaque lettre du mot secret
        if lettre in lettres_trouvees:  # Si la lettre est trouvée, on l'affiche
            affichage_du_mot = affichage_du_mot + lettre # On ajoute la lettre trouvée à l'affichage du mot
        else:
            affichage_du_mot = affichage_du_mot + "_" # On ajoute un _ si la lettre n'est pas trouvée

# Afficher l'état du mot
    print(dessins_pendu[8 - essais_restants]) # On affiche le dessin du pendu en fonction du nombre d'essais restants
    print("")
    print("Mot à deviner :", " ".join(affichage_du_mot)) # join permet de mettre un espace entre chaque lettre
    print("Il te reste", essais_restants, "essais.")
    print("")

    
# Vérifier si le joueur a gagné
    if "_" not in affichage_du_mot:
        print("Bravo ! Tu as gagné ! 🎉")
        break

# Demander une lettre
    proposition = input("Lettre ? ").lower() #.lower() permet de mettre la lettre en minuscule pour ne pas avoir de problème de majuscule/minuscule
    verifier_sortie(proposition) # On vérifie si l'utilisateur a entré 'exit'
    if len(proposition) != 1: #len(proposition) permet de savoir combien de lettres il y a dans la proposition et != 1 signifie qu'il n'y a qu'une seule lettre
        print("Merci d'entrer UNE seule lettre uniquement.")
        continue ## On continue la boucle si la condition n'est pas respectée
    if not proposition.isalpha(): #.isalpha() permet de savoir si la proposition est une lettre
        print("Veuillez entrer une lettre valide. (a-z ou A-Z)")
        continue

# Vérifier si la lettre a déjà été essayée
    if proposition in lettres_essayees:
        print("Tu as déjà essayé cette lettre.")
        continue
    lettres_essayees.append(proposition) # On ajoute la lettre essayée à la liste des lettres essayées

# Vérifier si la lettre est correcte
    if proposition in mot_secret:
        if proposition not in lettres_trouvees:
            print("Bonne réponse !")
            lettres_trouvees.append(proposition) # On ajoute la lettre trouvée à la liste des lettres trouvées
    else:
        print("Raté !")
        essais_restants = essais_restants - 1

 # Si tous les essais sont utilisés
if essais_restants == 0:
    print(dessins_pendu[8 - essais_restants])
    print("Perdu ! Le mot était :", mot_secret)