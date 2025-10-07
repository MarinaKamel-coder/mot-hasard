# 🔠 Jeu du Pendu – Devine le mot !

Un jeu classique du **Pendu** codé en **Python**, entièrement en console.  
Le but est simple : **deviner le mot secret avant que le pendu ne soit complet !**

---

## 🎯 Objectif du jeu

Le joueur doit deviner un **mot secret choisi au hasard** parmi une liste de mots.  
À chaque erreur, le dessin du pendu se complète petit à petit.  
Le joueur perd s’il fait **8 erreurs** avant d’avoir trouvé toutes les lettres.

---

## ⚙️ Fonctionnement

- Le programme choisit **un mot au hasard** parmi une liste :
  ```python
  mots = ["python", "programmation", "ordinateur", "developpeur"]

Vous proposez une lettre à chaque tour.

Si la lettre est :

✅ dans le mot → elle s’affiche.

❌ absente → vous perdez un essai.

Le dessin du pendu évolue à chaque mauvaise réponse.

Vous pouvez quitter le jeu à tout moment en tapant exit.
