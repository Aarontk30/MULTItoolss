# -*- coding: utf-8 -*-

# Copyright (c) RedTiger
# See the file 'LICENSE' for copying permission

import os
import sys
import importlib
import time

# Permet d'importer les modules des sous-dossiers
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from config.util import *
from config.config import *

def find_tools():
    """ Trouve dynamiquement les outils disponibles dans le dossier 'tools'. """
    tools_dir = 'tools'
    available_tools = []
    if os.path.exists(tools_dir):
        for filename in os.listdir(tools_dir):
            if filename.endswith('.py') and not filename.startswith('__'):
                available_tools.append(filename[:-3]) # Retire '.py'
    return available_tools

def main():
    """ Fonction principale qui affiche le menu et gère la sélection de l'outil. """
    while True:
        Title("Multi-Tool")
        Slow(map_banner)

        tools = find_tools()

        print(f"{BEFORE} Outils disponibles :{reset}")
        for i, tool_name in enumerate(tools, 1):
            formatted_name = tool_name.replace('_', ' ').replace('-', ' ').title()
            print(f"  {white}[{red}{i}{white}] {formatted_name}{reset}")

        print(f"  {white}[{red}0{white}] Quitter{reset}")

        try:
            choice_str = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Votre choix -> {reset}")
            choice = int(choice_str)

            if choice == 0:
                print(f"\n{INFO_ADD} Merci d'avoir utilisé le Multi-Tool. À bientôt !{reset}")
                break

            if 1 <= choice <= len(tools):
                selected_tool_name = tools[choice - 1]
                # Importe et exécute le module de l'outil sélectionné
                tool_module = importlib.import_module(f"tools.{selected_tool_name}")
                tool_module.run()
            else:
                print(f"\n{ERROR} Choix invalide. Veuillez réessayer.{reset}")
                time.sleep(2)

        except ValueError:
            print(f"\n{ERROR} Entrée invalide. Veuillez entrer un numéro.{reset}")
            time.sleep(2)
        except Exception as e:
            Error(e)

if __name__ == "__main__":
    main()
