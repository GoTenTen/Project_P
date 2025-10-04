# 🐾 POUKEMON (version Python)

Un jeu en ligne de commande où deux joueurs s’affrontent avec leurs équipes de **Pou**.  
Inspiré des mécaniques de Pokémon, il propose un combat stratégique avec attaques, boosts et gestion d’équipe.

---

## 📂 Structure du projet

```
.
├── ecran.py           # Menu d’accueil et règles
├── main.py            # Logique principale du jeu
├── battle.py          # Gestion des tours et des actions
├── class_poukemon.py  # Définition des Pou et des compétences génériques
├── competences.py     # Compétences disponibles (attaques, boosts, etc.)
└── team.py            # Gestion des équipes et changements de Pou
```

---

## ⚙️ Fonctionnement

1. **Lancement** :  
   ```bash
   python ecran.py
   ```
   Vous arrivez sur un menu avec 3 choix :  
   - Commencer  
   - Lire les règles  
   - Quitter  

2. **Création des équipes** :  
   Chaque joueur saisit son nom, puis reçoit automatiquement une équipe de Pou :  
   - **Pou** : 30 PV, 10 ATK  
   - **Gros Pou** : 50 PV, 7 ATK  
   - **Pipou Pou** : 20 PV, 15 ATK  

3. **Déroulement d’un combat** :  
   - L’ordre de jeu est tiré au hasard.  
   - Les joueurs jouent chacun leur tour.  
   - À chaque tour, un joueur peut :  
     - Attaquer (`Tape Fort` ou `Slap That Ass`)  
     - Se soigner (+10 PV)  
     - Booster son attaque (`Danse Lame`)  
     - Consulter la description des compétences  
     - Changer de Pou  

4. **Fin de partie** :  
   Quand une équipe n’a plus de Pou en vie, l’autre joueur gagne.  
   Un récapitulatif des actions est affiché à la fin du combat.

---

## 🧩 Exemple d’une partie (extrait console)

```
_________________________________________________

     █▀▀█ █▀▀█ █░░█ █░█ █▀▀ █▀▄▀█ █▀▀█ █▀▀▄
     █░░█ █░░█ █░░█ █▀▄ █▀▀ █░▀░█ █░░█ █░░█
     █▀▀▀ ▀▀▀▀ ░▀▀▀ ▀░▀ ▀▀▀ ▀░░░▀ ▀▀▀▀ ▀░░▀

                1 - COMMENCER
                2 - REGLES DU JEU
                3 - QUITTER
_________________________________________________

Veuillez définir le nom du Joueur 1 s'il vous plait. : Alice
Veuillez définir le nom du Joueur 2 s'il vous plait. : Bob

Qui commence entre Alice et Bob ?
...
Alice commence !

-------------- TOUR 1 --------------
[[Alice]]
- Pou : 30/30 PV | 10 ATK
- Gros Pou : 50/50 PV | 7 ATK
- Pipou Pou : 20/20 PV | 15 ATK

[[Bob]]
- Pou : 30/30 PV | 10 ATK
- Gros Pou : 50/50 PV | 7 ATK
- Pipou Pou : 20/20 PV | 15 ATK

C'est au tour de Alice avec Pou !

  1 - Attaquer (Tape Fort)
  2 - Se soigner (+10 PV)
  3 - Booster (Danse Lame)
  4 - Description des compétences
  5 - Changer de Pou
Votre choix : 1

Alice utilise Tape Fort et inflige 20 dégâts !
```

---

## 🛠️ Technologies utilisées

- **Python 3**  
- Bibliothèques standard : `time`, `random`

---

## 📌 Améliorations possibles

- Ajout de possibilité de choisir ses type d'attaques.
- Ajouter plus de Pou avec des statistiques variées.  
- Créer de nouvelles compétences (défensives, spéciales, etc.).  
- Intégrer une **IA** pour jouer en solo contre l’ordinateur.  
- Sauvegarder les scores ou l’historique des combats.  
- Créer une interface graphique (Tkinter, PyGame, ou autre).  

---

## 👨‍💻 Auteurs

Projet réalisé en Python par :  

- **GoTenTen**  
- **Kuanpheu**
