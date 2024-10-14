#importar las bibliotecas
import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt


#importar los datos del json

with open('mijson.json', 'r') as archivo:
    Camaguey = json.load(archivo)
Camaguey = pd.read_json('mijson.json')

# for i in Camaguey["mujeresPorAnnoCamaguey"].:
#     if(Camaguey["mujeresPorAnnoCamaguey"][i] == None): break
#     print(Camaguey["mujeresPorAnnoCamaguey"][i])

print(len(Camaguey["mujeresPorAnnoCamaguey"]))