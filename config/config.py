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
GEN_VALID = f"{white}[{green}SUCCESS{white}]{reset}"
GEN_INVALID = f"{white}[{magenta}ERROR{white}]{reset}"
BEFORE_GREEN = f"{white}[{green}+{white}]{reset}"
AFTER_GREEN = f"{white}[{green}+{white}]{reset}"


# --- WEBHOOK ---
username_webhook = "Crystal"
avatar_webhook = "https://cdn.discordapp.com/attachments/1114624133353840782/1114624974950375574/11-23-42-385_200-200-0-0_43261695420231-0.png"

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
