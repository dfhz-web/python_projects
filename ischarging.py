import psutil
import re

def is_charging():
    battery = psutil.sensors_battery()
    return battery.power_plugged

def get_battery_percentage():
    battery = psutil.sensors_battery()
    return battery.percent

if is_charging():
    print(f"El portátil está cargando y su carga actual es de {get_battery_percentage()}%.")
else:
    print(f"El portátil no está cargando y su carga actual es de {get_battery_percentage()}%.")