import requests
from bs4 import BeautifulSoup
import re


def dms_to_decimal(dms: str) -> float:
    parts = re.findall(r'\d+', dms)
    sign = -1 if 'S' in dms or 'W' in dms else 1
    degrees = float(parts[0])
    minutes = float(parts[1]) if len(parts) > 1 else 0
    seconds = float(parts[2]) if len(parts) > 2 else 0
    return sign * (degrees + minutes / 60 + seconds / 3600)


def get_coordinates(location: str) -> list[float]:
    url = f"https://pl.wikipedia.org/wiki/{location}"
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")

    geo = soup.find("span", class_="geo")
    if geo and ";" in geo.text:
        lat_str, lon_str = geo.text.strip().split(";")
        return [float(lat_str.strip()), float(lon_str.strip())]

    coords = soup.find("span", class_="coordinates")
    if coords:
        lat = coords.find("span", class_="latitude").text.strip()
        lon = coords.find("span", class_="longitude").text.strip()
        return [dms_to_decimal(lat), dms_to_decimal(lon)]

    raise ValueError(f"Nie znaleziono współrzędnych dla: {location}")
