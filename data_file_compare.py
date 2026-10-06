import pandas as pd 
from pathlib import Path 

def ingest(file1, file2):
    df1 = pd.read_csv(file1, sep=';')
    df2 = pd.read_csv(file2, sep=';')
    return df1, df2

def compare(df1, df2):
    df1_sorted = df1.sort_values(by=list(df1.columns)).reset_index(drop=True)
    df2_sorted = df2.sort_values(by=list(df2.columns)).reset_index(drop=True)
    sont_identiques = df1_sorted.equals(df2_sorted)
    return sont_identiques

def show_differences(df1, df2):
    comparaison = df1.merge(df2, how='outer', indicator=True)
    lignes_differentes = comparaison[comparaison['_merge'] != 'both']
    return lignes_differentes

if __name__ == "__main__":
  file_compare = Path("file_compare")

  file_list = list(file_compare.glob("*.csv"))
  if len(file_list) == 2:
    a, b = ingest(file_list[0], file_list[1])
    similaire = compare(a, b)

    if similaire == False:
      print("Liste des différences entre les fichiers:")
      print(show_differences(a, b))
    else:
      print("Les fichiers sont identiques")
  else:
    print("Merci de placer les 2 fichiers à comparer dans le dossier 'file_compare/'.")
