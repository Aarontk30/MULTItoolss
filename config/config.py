# -*- coding: utf-8 -*-

# Copyright (c) RedTiger
# See the file 'LICENSE' for copying permission

import colorama

# --- COLORS ---
blue = colorama.Fore.BLUE
magenta = colorama.Fore.MAGENTA
white = colorama.Fore.WHITE
green = colorama.Fore.GREEN
reset = colorama.Fore.RESET

# --- PREFIXES ---
BEFORE = f"{white}[{blue}+{white}]{reset}"
AFTER = f"{white}[{magenta}+{white}]{reset}"
INPUT = f"{white}[{blue}>{white}]{reset}"
WAIT = f"{white}[{magenta}WAIT{white}]{reset}"
INFO_ADD = f"{white}[{blue}INFO{white}]{reset}"
ERROR = f"{white}[{magenta}ERROR{white}]{reset}"
ADD = f"{white}[{blue}ADD{white}]{reset}"
INFO = f"{white}[{magenta}INFO{white}]{reset}"


# --- BANNERS ---
map_banner = f"""
{blue}
███╗   ███╗██╗   ██╗██╗ ██████╗ ██╗  ██╗
████╗ ████║██║   ██║██║██╔═══██╗╚██╗██╔╝
██╔████╔██║██║   ██║██║██║   ██║ ╚███╔╝
██║╚██╔╝██║██║   ██║██║██║   ██║ ██╔██╗
██║ ╚═╝ ██║╚██████╔╝██║╚██████╔╝██╔╝ ██╗
╚═╝     ╚═╝ ╚═════╝ ╚═╝ ╚═════╝ ╚═╝  ╚═╝
                        {white}--- Multi-Tool by Jules ---{reset}
"""

scan_banner = f"""
{magenta}
███████╗ ██████╗  █████╗ ███╗   ██╗
██╔════╝██╔════╝ ██╔══██╗████╗  ██║
███████╗██║  ███╗███████║██╔██╗ ██║
╚════██║██║   ██║██╔══██║██║╚██╗██║
███████║╚██████╔╝██║  ██║██║ ╚████║
╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝
                      {white}--- Web Scanner ---{reset}
"""
