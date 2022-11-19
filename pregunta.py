"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

    #
    # Inserte su código aquí
    #
    fileName = "clusters_report.txt"
    f = open(fileName, "r")
    lines = f.readlines()
    f.close()
    columns = [i.strip().lower().replace(' ', '_') for i in lines[0].strip().split('  ')]
    columns.remove('')
    clusters = []
    cantPalabras = []
    porcPalabras = []
    principalesPalabras = []
    for i in range(len(columns)):
        if i==1 or i==2:
            columns[i] = columns[i] + '_palabras_clave'
    del lines[:4]

    parrafo = 1
    palabras = []
    for line in lines:
        values = [item for item in line.split('  ') if item != '']
        if values == ['\n'] or values == [' \n']:
            parrafo = 1
            principalesPalabras.append(" ".join(palabras))
            palabras = []
            continue
        if parrafo == 1:
            clusters.append(int(values.pop(0).strip()))
            cantPalabras.append(int(values.pop(0).strip()))
            porcPalabras.append(float(values.pop(0)[:-2].strip().replace(",", ".")))
        values = [i.strip() for i in values]
        palabras.append(" ".join(values))
        parrafo += 1
    data = {
        columns[0]: clusters,
        columns[1]: cantPalabras,
        columns[2]: porcPalabras,
        columns[3]: principalesPalabras
    }
    df = pd.DataFrame(data)

    return df