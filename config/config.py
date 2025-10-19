# -*- coding: utf-8 -*-

# Copyright (c) RedTiger
# See the file 'LICENSE' for copying permission

import colorama

# --- COLORS ---
red = colorama.Fore.RED
white = colorama.Fore.WHITE
green = colorama.Fore.GREEN
reset = colorama.Fore.RESET

# --- PREFIXES ---
BEFORE = f"{white}[{red}+{white}]{reset}"
AFTER = f"{white}[{red}+{white}]{reset}"
INPUT = f"{white}[{red}>{white}]{reset}"
WAIT = f"{white}[{red}WAIT{white}]{reset}"
INFO_ADD = f"{white}[{red}INFO{white}]{reset}"
ERROR = f"{white}[{red}ERROR{white}]{reset}"

# --- BANNER ---
map_banner = f"""
{red}
██████╗ ███████╗██████╗     ████████╗ ██████╗  ██████╗ ██╗     ███████╗
██╔══██╗██╔════╝██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
██████╔╝█████╗  ██║  ██║       ██║   ██║   ██║██║   ██║██║     ███████╗
██╔══██╗██╔══╝  ██║  ██║       ██║   ██║   ██║██║   ██║██║     ╚════██║
██║  ██║███████╗██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
╚═╝  ╚═╝╚══════╝╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝

                {white}--- Welcome to the Multi-Tool by Jules ---{reset}
"""
