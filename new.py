#importar las bibliotecas
import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt


#importar los datos del json

with open('poblacionResidentePorAnnoCamaguey.json', 'r') as archivo:
    datos = json.load(archivo)
datos = pd.read_json('poblacionResidentePorAnnoCamaguey.json')

for clave in datos["poblacionResidentePorAnnoCamaguey"].keys():
    print(clave)
