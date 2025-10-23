import time
from Project_P.core.main import start
# ------------------------------------


def start_ecran():
    print('_________________________________________________')
    print('')
    print('')
    print('     █▀▀█ █▀▀█ █░░█ █░█ █▀▀ █▀▄▀█ █▀▀█ █▀▀▄')
    print('     █░░█ █░░█ █░░█ █▀▄ █▀▀ █░▀░█ █░░█ █░░█')
    print('     █▀▀▀ ▀▀▀▀ ░▀▀▀ ▀░▀ ▀▀▀ ▀░░░▀ ▀▀▀▀ ▀░░▀')
    print('')
    print('')
    print('                1 - COMMENCER')
    print('                2 - REGLES DU JEU')
    print('                3 - QUITTER')
    print('')
    print('_________________________________________________')

    time.sleep(1)
    x = str(input())
    while x not in ('1', '2', '3'):
        x = str(input())
        print('Choississez parmi 1,2 et 3\n')
    if x == '1':
        start()
    if x == '2':
        regles()
    if x == '3':
        exit()


def regles():
    print('                    REGLES                 ')
    print('')
    print('  Deux joueurs s\'affrontent dans un combat de ')
    print('poukemon, chacun de ces joueurs possède une ')
    print('équipe de 4 poukemon. ')
    print('  Chaque tour, les joueur doivent faire attaquer')
    print('à tour de rôle chacun de leurs poukemons.')
    print('  L\'ordre de passage des joueurs est defini au tout')
    print('début du jeu, aléatoirement.')
    print('')
    print('La partie est terminé lorsqu\'un joueur a tout ses')
    print('poukemons K.O .')

    time.sleep(2)

    def choix_regle():
        while True:
            x = input('Retourner au menu ? (Oui/Non) : ')
            if x.lower() == 'oui':
                return start_ecran()
            elif x.lower() == 'non':
                print('Une nouvelle fenêtre s\'affichera dans 5 secondes')
                time.sleep(5)
            else:
                print('Répondez uniquement par "Oui" ou par "Non" svp.')

    choix_regle()


start_ecran()
