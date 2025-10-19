# -*- coding: utf-8 -*-

# Copyright (c) RedTiger
# See the file 'LICENSE' for copying permission

from config.util import Slow, Title, current_time_hour, Continue, Reset, Error, ErrorModule
from config.config import map_banner, BEFORE, AFTER, INPUT, WAIT, INFO_ADD, red, white, reset
try:
    import requests
except Exception as e:
   ErrorModule(e)

def run():
    """ Fonction principale de l'outil Ip-Lookup. """
    Title("Ip Lookup")

    try:
        Slow(map_banner)
        ip = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Ip -> {reset}")
        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Recherche d'informations..")

        response = requests.get(f"http://ip-api.com/json/{ip}")
        api = response.json()

        status = "Valide" if api.get('status') == "success" else "Invalide"
        country = api.get('country', "None")
        country_code = api.get('countryCode', "None")
        region = api.get('regionName', "None")
        region_code = api.get('region', "None")
        zip_code = api.get('zip', "None")
        city = api.get('city', "None")
        latitude = api.get('lat', "None")
        longitude = api.get('lon', "None")
        timezone = api.get('timezone', "None")
        isp = api.get('isp', "None")
        org = api.get('org', "None")
        as_host = api.get('as', "None")

        Slow(f"""
{white}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 {INFO_ADD} Status    : {white}{status}{red}
 {INFO_ADD} Pays      : {white}{country} ({country_code}){red}
 {INFO_ADD} Région    : {white}{region} ({region_code}){red}
 {INFO_ADD} Code Postal: {white}{zip_code}{red}
 {INFO_ADD} Ville     : {white}{city}{red}
 {INFO_ADD} Latitude  : {white}{latitude}{red}
 {INFO_ADD} Longitude : {white}{longitude}{red}
 {INFO_ADD} Fuseau Hor. : {white}{timezone}{red}
 {INFO_ADD} FAI       : {white}{isp}{red}
 {INFO_ADD} Org       : {white}{org}{red}
 {INFO_ADD} As        : {white}{as_host}{red}{reset}
{white}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
""")

        Continue()
        Reset()
    except Exception as e:
        Error(e)

if __name__ == '__main__':
    run()
