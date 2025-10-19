# -*- coding: utf-8 -*-

# Copyright (c) RedTiger
# See the file 'LICENSE' for copying permission

import os
import sys
import time
from datetime import datetime
from .config import *

def Slow(text):
    """ Affiche le texte avec un effet de ralenti, caractère par caractère. """
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)
    print()

def Title(text):
    """ Efface la console et affiche un titre. """
    if os.name == 'nt': # Pour Windows
        os.system('cls')
    else: # Pour Mac et Linux
        os.system('clear')
    print(text)

def current_time_hour():
    """ Retourne l'heure actuelle au format HH:MM:SS. """
    return datetime.now().strftime('%H:%M:%S')

def Continue():
    """ Met le script en pause jusqu'à ce que l'utilisateur appuie sur Entrée. """
    input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Appuyez sur Entrée pour continuer -> {reset}")

def Reset():
    """ Redémarre le script principal. """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    # Cette fonction est conçue pour redémarrer le script.
    # Dans notre structure, nous la ferons simplement retourner au menu principal.
    # Pour l'instant, elle ne fera rien pour éviter de compliquer le code.
    pass

def ErrorModule(e):
    """ Affiche une erreur liée à un module manquant et quitte. """
    print(f"\n{ERROR} Une erreur est survenue lors de l'importation d'un module : {e}")
    print(f"{INFO_ADD} Veuillez installer les dépendances avec 'pip install -r requirements.txt'")
    sys.exit(1)

def Error(e):
    """ Affiche une erreur générique. """
    print(f"\n{ERROR} Une erreur inattendue est survenue : {e}")
    Continue()
    Reset()
